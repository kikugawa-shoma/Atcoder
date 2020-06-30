#include <bits/stdc++.h>

using namespace std;
using ll = long long;

int main(){
    int N,K;
    cin >> N >> K;
    vector<int> p(N);
    for (int i=0;i<N;i++)cin >> p[i];
    sort(p.begin(),p.end());
    ll sum = 0;
    for(int i=0;i<K;i++)sum += p[i];
    cout << sum << endl;


}