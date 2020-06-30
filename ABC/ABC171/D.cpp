#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ll N,Q; 
    cin >> N;
    vector<ll> A(N);
    for(ll i=0;i<N;i++)cin >> A[i];
    cin >> Q;
    vector<ll> B(Q),C(Q);
    for(ll i=0;i<Q;i++)cin >> B[i] >> C[i];

    unordered_map<ll ,ll> D;
    for(ll i=0;i<=100004;i++)D[i] = 0;
    for(ll i=0;i<N;i++)D[A[i]] += 1;
    ll sum = 0;
    for(ll i = 0;i<N;i++)sum += A[i];
    for(ll q=0;q<Q;q++){
        sum -= B[q]*D[B[q]];
        sum += C[q]*D[B[q]];
        D[C[q]] += D[B[q]];
        D[B[q]] = 0;
        cout << sum << endl;
    }
}