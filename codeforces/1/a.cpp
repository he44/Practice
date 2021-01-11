#include <iostream>

// (n // d) in Python
long long ceil(long long n, long long d)
{
    if (n % d)
    {
        return n / d + 1;
    } else 
    {
        return n / d;
    }
}

int main()
{
    long long n, m, a;
    std::cin >> n >> m >> a;
    std::cout << ceil(n,a) * ceil(m, a);
    return 0;
}
