#include <iostream>
#include <string>

char to_lower(char c)
{
    if (c < 'a')
    {
        return c;
    } else 
    {
        return (c - 'a') + 'A';
    }
}

int main()
{
    std::string a, b;
    std::cin >> a >> b;
    int n = a.size();
    char ca, cb;
    for (int i = 0; i < n; ++i)
    {
        ca = to_lower(a[i]);
        cb = to_lower(b[i]);
        if (ca < cb)
        {
            std::cout << -1;
            return 0;
        } else if (ca > cb)
        {
            std::cout << 1;
            return 0;
        }
    }
    std::cout << 0;
    return 0;
}
