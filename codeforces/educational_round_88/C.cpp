#include <iostream>
#include <cmath>

int main(){
    using namespace std;
    int t;
    cin >> t;
    int h,c,tar;
    int ret;
    float kp;
    for (int i = 0; i < t; ++i){
        cin >> h >> c >> tar;
        float avg = (float) (h+c) / 2.0;
        // trivial case
        if (tar <= avg){
            ret = 2;
        } else {
            kp = (float)(tar-h) / (float)(c+h-2 * tar);
            int c1 = int(kp);
            int c2 = c1 + 1;
            // compare the results with c1 and c2
            float d1 = abs(((c1 + 1.0) * h + (float)c1 * c) / (2.0 * c1 + 1) - tar);
            float d2 = abs(((c2 + 1.0) * h + (float)c2 * c) / (2.0 * c2 + 1) - tar);
            // c1 is the smaller one, so if d1 and d2 are equal, choose c1
            int k = (d1 <= d2)?c1:c2;
            ret = 2 * k + 1;
        }
        cout << ret << endl;
    }
    return 0;
}
