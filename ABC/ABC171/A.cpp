#include <iostream>

using namespace std;

int main(){
    char alpha;
    cin >> alpha;
    int x = int(alpha);
    if (int('a') <= x && x <= int('z'))cout << 'a' << endl;
    else cout << 'A' << endl;
}