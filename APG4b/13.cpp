#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    for(int i=0;i<N;i++)cin >> A[i];
    int mean = 0;
    for(int i=0;i<N;i++)mean+=A[i];
    mean /=N;
    for(int i=0;i<N;i++)cout << abs(mean-A[i]) << endl;
}