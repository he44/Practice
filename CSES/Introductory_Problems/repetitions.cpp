#include<iostream>

int main()
{
    std::string seq;
    std::cin >> seq;

    int ans = 1;
    auto cur = seq[0];
    int len = 1;

    for (int i = 1; i < seq.size(); ++i)
    {
        if (seq[i] == cur)
        {
            len += 1;
        } else 
        {
            ans = (len > ans)?len:ans;
            cur = seq[i];
            len = 1;
        }
        //std::cout << "i is " << i;
        //std::cout << " len is " << len;
        //std::cout << " ans is " << ans << std::endl;
    }
    ans = (len > ans)?len:ans;
    std::cout << ans;
    return 0;
}
