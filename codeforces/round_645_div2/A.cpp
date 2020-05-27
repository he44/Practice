#include <iostream>
#include <vector>
using namespace std;

int main(){
    int t, m, n;
    int k;
    cin >> t;
    for (int i = 0; i < t; ++i){
        cin >> m >> n;
        int res = 0;
        k = n / 2;
        res += m * k;
        if (n%2){
            int tmp = (m%2)?(m/2+1):(m/2);
            res += tmp;
        }
        cout << res << endl;
    }
}
