#include<bits/stdc++.h>
using namespace std;

void bar(int n,char name){
    int i=0;
    cout << name << ':';
    while(i++<n)cout << ']';
    cout << endl;
}

int main(){
    int a,b;
    cin >> a >> b;
    bar(a,'A');
    bar(b,'B');
}