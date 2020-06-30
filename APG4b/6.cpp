#include<bits/stdc++.h>
using namespace std;

int main(){
    int a,b;
    char op;
    string er = "error";
    cin >> a >> op >> b;
    if(op == '+')cout << a+b;
    else if(op == '-')cout << a-b;
    else if(op == '*')cout << a*b;
    else if(op == '/'){
        if(b == 0)cout << er;
        else cout << a/b;
    }
    else cout << er;
    cout << endl;
    
}