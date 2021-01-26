#include<iostream>

int main()
{
    long long n;
    std::cin >> n;
    long long sum = n * (n + 1) / 2;
    long long a;
    for (int i = 0; i < n - 1; ++i)
    {
        std::cin >> a;
        sum -= a;
    }
    std::cout << sum;
    return 0;
}
