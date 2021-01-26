#include<iostream>
#define ll long long

int main()
{
    int n;
    std::cin >> n;
    ll largest = 0;
    ll cur = 0;
    ll ans = 0;
    for (int i = 0; i < n; ++i)
    {
        std::cin >> cur;
        ans = (largest > cur)?(ans + (largest - cur)):(ans);
        largest = (largest > cur)?largest:cur;
    }
    std::cout << ans;


    return 0;
}
