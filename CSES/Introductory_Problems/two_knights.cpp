#include<iostream>
#define ll long long

int main()
{
    int n;
    std::cin >> n;
    for (int i = 1; i < n + 1; ++i)
    {
        ll pos_num = i * i;
        ll ans = pos_num * (pos_num - 1) / 2; // total number of ways
        ans -= 2 * 2 * (i - 1) * (i - 2); // subtracting attack positions
        std::cout << ans << std::endl;
    }

    return 0;
}
