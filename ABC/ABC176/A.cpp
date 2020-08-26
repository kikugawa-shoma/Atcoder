#define _GLIBCXX_DEBUG
#define rep(i,n) for(int i=0;i<(n);i++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    int N,X,T;
    cin >> N >> X >> T;
    cout << ((N + X - 1)/X)*T << endl;
}