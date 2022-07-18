#include"bits/stdc++.h"
using namespace std;

#define ll long long
#define pii pair<int,int>
#define ff first
#define ss second
#define endll '\n'
#define rep(i,n) for(int i=0;i++<n;)
#define scl(i) scanf("%lld",&i)
#define int long long int
#define all(n) n.begin(),n.end()
#define mem(n,i) memset(n,i,sizeof n)
#define em(a) emplace_back(a)
#define pb(a) push_back(a)
#define srep(it,vv) for(auto &it : vv)
#define prep(it,vv) for(auto it : vv)
#define b_s(a,b) binary_search(a.begin(),a.end(),b)
#define l_b(a,b) lower_bound(a.begin(),a.end(),b)
#define u_b(a,b) upper_bound(a.begin(),a.end(),b)
//vector<vector<int>>arr(n + 5, vector<int>(m + 5,0));

typedef vector<int> vii;
typedef vector<string> vss;
/*

*/

int min_value(vii Ai, vii human, int alpha, int beta,int f);
int max_value(vii Ai, vii human, int alpha, int beta,int f);



int heuristic1(vii x, vii y)
{
    int sum1 = 0,sum2=0;
    for(int i=1; i<=6; i++)
        sum1+=x[i];
    for(int i=1; i<=6; i++)
        sum2+=y[i];

    if(x[7]>=y[0] and sum1<=sum2)
        return x[7]+sum1;
    return x[0];
}
int heuristic2(vii x, vii y)
{
    int sum1 = 0,sum2=0;
    for(int i=1; i<=6; i++)
        sum1+=x[i];
    for(int i=1; i<=6; i++)
        sum2+=y[i];

    if(x[7]<=y[0] and sum1>=sum2)
        return y[0]+sum2;
    return y[0];
}



bool goaltest(vii a,vii b)
{
    int sum1 = 0,sum2 = 0;
    for(int i=1; i<=6; i++)
        sum1+=a[i];
    for(int i=1; i<=6; i++)
        sum2+=b[i];

    if(sum1==0 or sum2==0)
        return true;
    return false;
}



/// human array = [ 0 1 2 3 4 5 6 7] /// 0 is store box
/// AI array =    [ 0 1 2 3 4 5 6 7] /// 7 is store box

/// a is AI
/// b is human
/// idx is ami akhon kotna index er ghuti distribute korbo
/// f is choosing AI or human
/// f = 0 AI
/// f = 1 human
bool call(vii &a, vii &b,int idx,int f)
{
    if(f==0)
    {
        int kon_box = 0;// 0 mean AI box and 1 is human box
        int ghuti = a[idx];
        a[idx] = 0;

        while(ghuti)
        {
            if(kon_box==0)
            {
                idx++;
                if(idx>7)
                {
                    kon_box = 1;
                    idx=6;
                }
            }
            else
            {
                idx--;
                if(idx<=0)
                {
                    kon_box = 0;
                    idx=1;
                }
            }



            if(ghuti!=1)
            {
                if(kon_box==0)
                    a[idx]++;
                else
                    b[idx]++;
            }
            else
            {
                if(kon_box==1)
                    b[idx]++;
                else
                {
                    if(idx==7)
                    {
                        a[idx]++;
                        return true; /// return true means you will get extra move
                    }
                    else if(a[idx]==0)
                    {
                        if(b[idx])
                        {
                            a[7] += 1+b[idx];
                            b[idx]=0;
                        }
                        else
                            a[idx]++;
                    }
                    else
                        a[idx]++;
                }
            }
            ghuti--;
        }
    }
    else
    {
        int kon_box = 1;
        int ghuti = b[idx];
        b[idx] = 0;

        while(ghuti)
        {
            if(kon_box==0)
            {
                idx++;
                if(idx>=7)
                {
                    kon_box = 1;
                    idx=6;
                }
            }
            else
            {
                idx--;
                if(idx<0)
                {
                    kon_box = 0;
                    idx=1;
                }
            }



            if(ghuti!=1)
            {
                if(kon_box==0)
                    a[idx]++;
                else
                    b[idx]++;
            }
            else
            {
                if(kon_box==0)
                    a[idx]++;
                else
                {
                    if(idx==0)
                    {
                        b[idx]++;
                        return true;/// return true means you will get extra move
                    }
                    else if(b[idx]==0)
                    {
                        if(a[idx])
                        {
                            b[0] += 1+a[idx];
                            a[idx]=0;
                        }
                        else
                            b[idx]++;
                    }
                    else
                        b[idx]++;
                }
            }
            ghuti--;
        }
    }
    return false;
}

// AI max
// HUMAN min

int lvl=5;

int max_value(vii AI, vii human, int alpha, int beta, int level)
{
    if(goaltest(AI,human))
    {
        return -AI[7];
    }

    if(level==0)
    {
        return -heuristic1(AI,human);
    }
    int idx = 0;
    for(int i=1; i<=6; i++)
    {
        if(AI[i]==0)
            continue;

        vii temp_AI = AI;
        vii temp_human = human;

        while(1)
        {
            if(goaltest(temp_AI,temp_human))
                break;
            if(!call(temp_AI,temp_human,i,0))
                break;
        }
        int xx = min_value(temp_AI,temp_human,alpha,beta,level-1);

        if(beta!=0)
        {
            if(xx>=beta)
                return 1000000000;
        }

        if(alpha==0)
            alpha = xx;
        if(xx>=alpha)
            idx = i,alpha=xx;
    }

    if(level==lvl)
        return idx;
    return alpha;

}
int min_value(vii AI, vii human, int alpha, int beta,int level)
{
    if(goaltest(AI,human))
    {
        return AI[7];
    }

    if(level==0)
    {
        return heuristic2(AI,human);
    }
    for(int i=1; i<=6; i++)
    {
        if(human[i]==0)
            continue;
        vii temp_AI = AI;
        vii temp_human = human;

        while(1)
        {
            if(goaltest(temp_AI,temp_human))
                break;
            if(!call(temp_AI,temp_human,i,1))
                break;
        }

        int xx = max_value(temp_AI,temp_human,alpha,beta,level-1);
        if(alpha!=0)
        {
            if(xx<=alpha)
                return -xx;
        }
        if(beta==0)
            beta = xx;
        beta = min(beta,xx);
    }

    return beta;
}

void print_vector(vii a,vii b)
{
    cout<<endl;
    cout<<"  ";
    for(int i=1; i<=6; i++)
        cout<<b[i]<<' ';
    cout<<"      <---Human";
    cout<<endll;
    cout<<b[0]<<"             "<<a[7]<<endll;

    cout<<"  ";
    for(int i=1; i<=6; i++)
        cout<<a[i]<<' ';
    cout<<"      <---Computer";
    cout<<endl<<endl;
}

signed main()
{
    cout<<"\n--------------Mancala using Alpha-Beta Pruning--------\n";
    vii v2 = {0,4,4,4,4,4,4,0};
    vii v1 = {0,4,4,4,4,4,4,0};
    int f = 0;/// f==0 human move, f==1 means AI move
    print_vector(v1,v2);
    while(!goaltest(v1,v2))
    {
        if(f==0)
        {
            cout<<"Human Turns choose(1-6): ";
            int n;
            cin>>n;
            if(v2[n])
            {
                bool xx = call(v1,v2,n,1);
                print_vector(v1,v2);
                if(xx==false)f^=1;
            }
            else
                cout<<"Invalid choice\n";
        }
        else
        {
            cout<<"Computer Choose : ";
            int d = max_value(v1,v2,0,0,lvl);
            cout<<d<<endll;
            bool xx = call(v1,v2,d,0);
            print_vector(v1,v2);
            if(xx==false)f^=1;
        }
    }

    rep(i,6) v1[7] += v1[i];
    rep(i,6) v2[0] += v2[i];

    if(v1[7]>v2[0]) cout<<endl<<endl<<"----------Computer WIN!!-----"<<endl<<endl;
    else if(v1[7]==v2[0]) cout<<endl<<endl<<"----------Game DRAW!!-----"<<endl<<endl;
    else cout<<endl<<endl<<"----------Human WIN!!-----"<<endl<<endl;

    //call(v1,v2,4,0);
    //cout<<endl<<max_value(v1,v2,0,0,lvl)<<endll;
    //print_vector(v1,v2);
}






