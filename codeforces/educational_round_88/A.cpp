#include <iostream>

int main(){
    using namespace std;
    int t;
    int n, m, k;
    int nc;
    cin >> t;
    for (int i = 0; i < t; ++i){
        cin >> n >> m >> k;
        nc = n/k;
        int pt = 0;
        if (nc >= m){
            pt = m;
        } else {
            int oc = (m - nc) / (k-1);
            if ((m-nc)%(k-1)){
                oc += 1;
            }
            pt = nc - oc;
        }
        cout << pt << endl;
    }
    return 0;
}
