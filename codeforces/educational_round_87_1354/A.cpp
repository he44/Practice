#include <iostream>
using namespace std;

int main(){
    int t;
    long long a, b, c, d;
    long long round;
    long long ans;
    cin >> t;
    for (int i = 0; i < t; ++i){
        cin >> a >> b >> c >> d;
        // enough sleep on the first trail
        if (a <= b){
            cout << b << endl;
            continue;
        }
        if ((a > b) && (c-d)<=0){
            cout << -1 << endl;
            continue;
        }
        round = (a-b)/(c-d);
        if ((a-b)%(c-d)){
            round += 1;
        }
        ans = b + round * c;
        cout << ans << endl;
    }
    return 0;
}
