#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int sum(vector<int> scores){
    int S = 0;
    for(int i=0;i<scores.size();i++)S += scores[i];
    return S;
}

void output(int sum_a,int sum_b,int sum_c){
    cout << sum_a*sum_b*sum_c << endl;
}

vector<int> input(int N){
    vector<int> scores(N);
    for(int i=0;i<N;i++)cin >> scores[i];
    return scores;
}

int main(){
    int N;
    cin >> N;

    vector<int> A = input(N);
    vector<int> B = input(N);
    vector<int> C = input(N);

    int sum_a = sum(A);
    int sum_b = sum(B);
    int sum_c = sum(C);

    output(sum_a,sum_b,sum_c);
}