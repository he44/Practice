#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int count = 0;
    for (int i = 0; i < n; ++i){
        int p,v,t;
        std::cin >> p;
        std::cin >> v;
        std::cin >> t;
        if (p + v + t >= 2){
            count += 1;
        }
    }
    std::cout << count;
    return 0;
}
