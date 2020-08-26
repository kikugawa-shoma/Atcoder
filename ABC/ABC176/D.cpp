#define _GLIBCXX_DEBUG
#define rep(i,n) for(int i=0;i<(n);i++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int H,W,Ch,Cw,Dh,Dw;

bool is_in_map(int h,int w){
    return (h >= 0 && h < H && w >= 0 && w < W);
}

bool is_movable(int h,int w,char c){
    return c=='.';
}

bool is_move_A(int i,int j){
    return ((i==0&&(j==-1 || j==1)) || (j==0 && (i==-1 || i==1)));
}

int main(){
    
    cin >> H >> W;
    cin >> Ch >> Cw;
    cin >> Dh >> Dw;
    --Ch;--Cw;--Dh;--Dw;
    vector<string> S(H);
    rep(i,H) cin >> S[i];
    

    int INF = 1000000000;
    
    vector<vector<int>> cost(H,vector<int>(W,INF));
    vector<vector<bool>> searched(H,vector<bool>(W,false));

    
    deque<array<int,3>> q(0,array<int,3>());
    array<int,3> pos{Ch,Cw,0};
    q.push_front(pos);
    while(!q.empty()){
        int w,h,c;
        
        h = q.front()[0];
        w = q.front()[1];
        c = q.front()[2];
        q.pop_front();
        searched[h][w] = true;

        for(int i=-2;i<3;i++){
            for(int j=-2;j<3;j++){
                int next_h,next_w;
                next_h = h + i;
                next_w = w + j;
                if(!is_in_map(next_h,next_w) || !is_movable(next_h,next_w,S[next_h][next_w]))continue;
                if(!searched[next_h][next_w]){
                    if(is_move_A(i,j)){
                        pos[0] = next_h;pos[1] = next_w;pos[2] = c;
                        q.push_front(pos);
                        cost[next_h][next_w] = min(cost[next_h][next_w],c);
                    }
                    else{
                        pos[0] = next_h;pos[1] = next_w;pos[2] = c+1;
                        q.push_back(pos) ;
                        cost[next_h][next_w] = min(cost[next_h][next_w],c+1);
                    }
                }

            }
        }
    }
    if(searched[Dh][Dw])cout << cost[Dh][Dw] << endl;
    else cout << -1 << endl;
}