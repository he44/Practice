#include <iostream>
#include <vector>

int main()
{
    int M, N;
    std::cin >> M >> N;
    int good_num = M / 2;
    int bad_num = N / 2;
    int ans = M % 2 == 0?good_num * N:good_num * N + bad_num;
    std::cout << ans << std::endl;
    return 0;
}
