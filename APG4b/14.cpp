#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> abc(3);
    for(int i=0;i<3;i++)cin >> abc[i];
    sort(abc.begin(),abc.end());
    cout << abc[2] - abc[0] << endl;
}