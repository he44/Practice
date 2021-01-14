#include <iostream>
#include <vector>

int main()
{
    std::string input;
    std::cin >> input;
    std::vector<int> counts(3, 0);
    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] == '+')
        {
            continue;
        } else
        {
            counts[input[i] - '1'] += 1;
        }
    }
    bool first = true;
    for (int i = 0; i < counts.size(); ++i)
    {
        for (int j = 0; j < counts[i]; ++j)
        {
            if (!first)
            {
                std::cout << "+";
            }
            std::cout << (char('1' + i));
            first = false;
        }
    }
    return 0;
}
