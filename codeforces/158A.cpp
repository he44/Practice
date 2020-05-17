#include <iostream>
#include <vector>
#include <algorithm>


int main(){
    int n,k;
    std::cin >> n;
    std::cin >> k;

    std::vector<int> scores;
    int score;
    for (int i = 0; i < n; ++i){
        std::cin >> score;
        scores.push_back(score);
    }

    std::sort(scores.begin(), scores.end(), std::greater<>());
    
    int count = 0;
    int thres = scores[k-1];
    for (int i = 0; i < n; ++i){
        if (scores[i] <= 0 || scores[i] < thres){
            break;
        }
        count += 1;
    }

    std::cout << count << std::endl;
    return 0;
}
