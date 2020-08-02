#include <iostream>

int main()
{
    int n = 0;
    int x = 0;
    std::cin >> n;
    for (int i = 0; i < n; ++i)
    {
        std::string command;
        std::cin >> command;
        for (int j = 0; j < command.length(); ++j)
        {
            if (command[j] == '+') // single quote, char vs char
            {
                x += 1;
                break;
            } else if (command[j] == '-')
            {
                x -= 1;
                break;
            }
        }
    }
    std::cout << x << std::endl;
    return 0;
}