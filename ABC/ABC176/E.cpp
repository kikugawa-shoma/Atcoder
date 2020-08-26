#define _GLIBCXX_DEBUG
#define rep(i,n) for(int i=0;i<(n);i++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    int h,w,m;
    cin >> h >> w >> m;
    vector<pair<int,int>> bomb(m);
    rep(i,m){
        cin >> bomb[i].first >> bomb[i].second;
        --bomb[i].first;--bomb[i].second;
    }

    vector<int> r(h,0);
    vector<int> c(w,0);

    rep(i,m){
        r[bomb[i].first]++;
        c[bomb[i].second]++;
    }

    int rmax = *max_element(r.begin(),r.end());
    int cmax = *max_element(c.begin(),c.end());

    set<int> max_r_inds;
    set<int> max_c_inds;

    rep(i,h)if(r[i] == rmax)max_r_inds.insert(i);
    rep(i,w)if(c[i] == cmax)max_c_inds.insert(i);

    ll cross_bomb_cnt = 0;
    ll cross = max_r_inds.size()*max_c_inds.size();

    rep(i,m){
        if(max_r_inds.count(bomb[i].first)){
            if(max_c_inds.count(bomb[i].second)){
                cross_bomb_cnt++;
            }
        }
    }
    
    if(cross_bomb_cnt < cross)cout << rmax + cmax;
    else cout << rmax + cmax - 1;
    cout << endl;


}