//1 testcase WA
// I cannot specify the reason

#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    int N,Q;
    cin >> N >> Q;
    vector<int> A(N),B(N);
    vector<int> C(Q),D(Q);
    for(int i=0;i<N;i++)cin >> A[i] >> B[i];
    for(int i=0;i<Q;i++)cin >> C[i] >> D[i];

    vector<multiset<int>> kg(200010);//kindergerden
    for(int i=0;i<N;i++)kg[B[i]].insert(A[i]);
    multiset<int> fairness;

    for(int i=1;i<=200000;i++){
        if(!kg[i].empty())fairness.insert(*--kg[i].end());
    }

    for(int q=0;q<Q;q++){
        int rate = A[C[q]-1];
        int pre_kg = B[C[q]-1];
        int next_kg = D[q];

        B[C[q]-1] = D[q];

        fairness.erase(fairness.find(*--kg[pre_kg].end()));
        if(!kg[next_kg].empty())fairness.erase(fairness.find(*--kg[next_kg].end()));

        kg[pre_kg].erase(kg[pre_kg].find(rate));
        kg[next_kg].insert(rate);
        
        if(!kg[pre_kg].empty())fairness.insert(*--kg[pre_kg].end());
        fairness.insert(*--kg[next_kg].end());

        cout << *fairness.begin() << endl;
    }

}