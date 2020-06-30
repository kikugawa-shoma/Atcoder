#include<bits/stdc++.h>
using namespace std;

int main(){
    int N,a,b;
    char op;
    cin >> N >> a;
    for(int i=0;i<N;i++){
        cin >> op >> b;
        string er = "error";
        if(op == '/'){
            if(b == 0){
                cout << er << endl;
                break;
            }
            a /= b;
        }
        if(op == '+')a += b;
        if(op == '-')a -= b;
        if(op == '*')a *= b;
        cout << i+1 << ':' << a << endl;
    }
}