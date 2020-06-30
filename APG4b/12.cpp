#include <bits/stdc++.h>
using namespace std;
int main(){
    string S;
    cin >> S;

    int n = S.size()/2;
    int ans = 1;
    for(int i=0;i<n;i++){
        if(S.at(2*i+1) == '+')ans+=1;
        else ans-=1;
    }
    cout << ans << endl;
}