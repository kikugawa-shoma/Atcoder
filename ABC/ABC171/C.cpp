#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ll N;
    cin >> N;

    vector<ll> pows(100);
    pows[0] = 26;
    for(int i=1;i<100;i++)pows[i] = pows[i-1]*26;

    int keta;
    for(int i=0;i<100;i++){
        if(N > pows[i]){
            N -= pows[i];
            continue;
        }
        keta = i+1;
        break;
    }

    N -= 1;
    vector<char> ans(keta);
    for(int i=0;i<keta;i++){
        ans[i] = char(N%26 + int('a'));
        N /= 26;
    }
    for(int i=0;i<keta;i++)cout << ans[keta-i-1];
    cout << endl;
}