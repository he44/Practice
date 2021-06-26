#include <iostream>


int main()
{

    auto compare = [](auto x){return x < 24;};
    int a = 32;
    int b = 42;
    float c = 32.4;
    float d = 16;
    std::cout << compare(a) << std::endl;
    std::cout << compare(b) << std::endl;
    std::cout << compare(c) << std::endl;
    std::cout << compare(d) << std::endl;

}
