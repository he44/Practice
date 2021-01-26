#include<iostream>
#define ll long long


int main()
{
    ll n;
    std::cin >> n;
    if (n == 1)
    {
        std::cout << 1;
    } else if (n <= 3)
    {
        std::cout << "NO SOLUTION";
    } else 
    {
        bool flipped = false;
        ll num = 2;
        for (ll i = 0; i < n; ++i)
        {
            if (num > n)
            {
                if (flipped) {break;}
                else {
                    num = 1;
                }
            }
            std::cout << num << " ";
            num += 2;
        }
    }

    return 0;
}
