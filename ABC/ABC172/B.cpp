#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main(){
    string S,T;
    cin >> S >> T;
    int cnt = 0;
    for(int i=0;i<S.size();i++){
        if(S[i] != T[i])cnt++;
    }
    cout << cnt << endl;
}