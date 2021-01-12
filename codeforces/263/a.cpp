#include <iostream>

int main()
{
    int row = 0;
    int col = 0;
    // Manhattan Distance
    while (row < 5)
    {
        int a = 0;
        col = 0;
        while (col < 5)
        {
            std::cin >> a;
            //std::cout << a << "@" << col << std::endl;
            if (a == 1)
            {
                break;
            }
            col += 1;
        }
        if (a == 1)
        {
            break;
        }
        row += 1;
    }
    //std::cout << row << " " << col;
    std::cout << abs(row - 2) + abs(col - 2);
    return 0;
}
