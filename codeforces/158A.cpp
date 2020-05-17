#include <iostream>
#include <vector>
using namespace std;


int main(){
    int n,k;

    cin >> n;
    cin >> k;
    cout << n << endl;
    cout << k << endl;
    return 0;
    vector<int> scores;
    int score;
    for (int i = 0; i <= n; ++i){
        cin >> score;
        scores.push_back(score);
    }
    sort(scores.begin(), scores.end());
    /*
    for (auto & i:scores){
        cout << i << endl;
    }
    */
    return 0;
}
