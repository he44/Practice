#include<iostream>
#define ll long long

int main()
{
    ll t;
    std::cin >> t;
    ll x, y;
    ll ans;
    ll n;
    while (t > 0)
    {
        std::cin >> y >> x;
        n = std::max(y,x);
        // bottom right corner of each layer (diagonal term of the matrix)
        // difference is a arithmetic series, 
        // nth layer will have 1 + 2 + 4 + ... + 2(n-1) at bottom right corner
        ll br = 1 + n * (n - 1);
        if (n % 2)
        {
            ans = br + x - y;
        } else {
            ans = br - x + y;
        }
        std::cout << ans << std::endl;
        t -= 1;
    }

    return 0;
}
