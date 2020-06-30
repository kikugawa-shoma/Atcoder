#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    long int N,M,K; 
    cin >> N >> M >> K;
    vector<ll> A(N),B(M),S_A(N+1),S_B(M+1);
    for(int i=0;i<N;i++)cin >> A[i];
    for(int i=0;i<M;i++)cin >> B[i];
    for(int i=0;i<N;i++)S_A[i+1] = S_A[i]+A[i];
    for(int i=0;i<M;i++)S_B[i+1] = S_B[i]+B[i];
    S_B.push_back(1000000010);
    int ans = 0;
    for(int i=0;i<N+1;i++){
        ll rest = K-S_A[i];
        if(rest >= 0){
            int l=0,r=M+1,m;
            while(r-l>1){
                m = (l+r)/2;
                if(S_B[m]>rest)r = m;
                else l = m;
            }
            ans = max(ans,i+l);
        }
    }
    cout << ans << endl;

}