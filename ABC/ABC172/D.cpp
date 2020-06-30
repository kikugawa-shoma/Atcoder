#define _glibcxx_debug
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    long n;
    cin >> n;
    
    vector<ll> f(n+1);
    for(long i=1;i<=n;i++){
        for(long j=1;j<=n;j++){
            if(j*i>n)break;
            f[j*i] += 1;
        }
    }
    ll ans=0;
    for(int i=1;i<=n;i++)ans += i*f[i];
    cout << ans << endl;
}