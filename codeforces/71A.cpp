#include <iostream>
#include <string>
#include <vector>
int main()
{
	int n;
	std::cin >> n;
	std::string s;
	for (int i = 0; i < n; i++){
		std::cin >> s;
		int len = s.size();
		if (len > 10){
			std::string ns;
			ns = s[0] + std::to_string(len-2) + s.back();
			std::cout << ns << std::endl;
		} else {
			std::cout << s << std::endl;
		}
	}
		
}

