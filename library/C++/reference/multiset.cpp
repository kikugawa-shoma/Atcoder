#define _GLIBCXX_DEBUG
#define rep(i,n) for(int i=0;i<(n);i++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    multiset<int> A = {1,2,2,4,7,2,3,2,2,2};
    cout << "multiset<int> A = {1,2,2,4,7,2,3,2,2,2};" << endl;

    for(auto itr = A.begin();itr != A.end();itr++)cout << *itr;
    cout << " : malutiset is auto sorted" << endl;

    A.erase(A.find(2));
    for(auto itr = A.begin();itr != A.end();itr++)cout << *itr;
    cout << " : A.erase(A.find(2)) erase one 2" << endl;

    A.erase(2);
    for(auto itr = A.begin();itr != A.end();itr++)cout << *itr;
    cout <<  " : A.erase(2) erase all 2!" << endl;

    cout << "*A.begin() : " << *A.begin() << endl;

    cout << "*A.rbegin() : " << *A.rbegin() << endl;

    cout << "*--A.end() : " << *--A.end() << endl;

    cout << "*--A.rend() : " << *--A.rend() << endl;

}