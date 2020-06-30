#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main(){
    int N = 5;
    vector<int> A(N);
    for(int i=0;i<N;i++)cin >> A[i];
    bool f = false;
    for(int i=1;i<N;i++){
        if(A[i-1] == A[i]){
            f = true;
            break;
        }
    }
    if(f)cout << "YES";
    else cout << "NO";
    cout << endl;
}