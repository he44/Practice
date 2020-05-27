#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int t, n;
    cin >> t;
    for (int i = 0; i < t; ++i){
        cin >> n;
        vector<int> a;
        int ai;
        for (int j = 0; j < n; ++j){
            cin >> ai;
            a.push_back(ai);
        }

        // sort array a
        sort(a.begin(), a.end());
        int come = 1;
        for (int k = a.size() - 1; k >= 0; --k){
            if (a[k] <= k + 1){
                come += (k+1);
                break;
            }
        }
        cout << come << endl;
    }

}
