#include <iostream>
#include <vector>
#include <string>

int main(){
    using namespace std;
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i){
        int n, m, x, y;
        
        cin >> n >> m >> x >> y;
        bool cheaper = (2 * x < y);
        string tiles;
        int cost = 0;
        int tmp = 0;
        for (int r = 0; r < n; ++r){
            cin >> tiles;
            int prev_w = -2;
            for (int c = 0; c < m; ++c){
                if (tiles[c] == '.') {
                    if (prev_w == c - 1){
                        tmp = (cheaper)?(2 * x):(y);
                        cost += (tmp - x);
                        prev_w = -2;
                    } else {
                        prev_w = c;
                        cost += x;
                    }
                }
            }
        }
        cout << cost << endl;
    }
    return 0;
}
