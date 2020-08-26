#define _GLIBCXX_DEBUG
#define rep(i,n) for(int i=0;i<(n);i++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    int N;
    cin >> N;
    vector<ll> A(N);
    rep(i,N)cin >> A[i];
    ll M = 0,dai = 0;
    rep(i,N){
        if(A[i]<M)dai += M - A[i];
        M = max(M,A[i]);
    }
    cout << dai << endl;

}