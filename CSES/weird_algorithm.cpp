#include <iostream>
int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    long long n;
    std::cin >> n;
    while (n != 1)
    {
        std::cout << n << " ";
        if (n % 2 == 1)
        {
            n = 3 * n + 1;
        } else 
        {
            n/=2;
        }
    }
    std::cout << n << " ";
    return 0;
}
