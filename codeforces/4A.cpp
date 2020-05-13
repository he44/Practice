#include <iostream>
int main(){
	int input;
	std::cin >> input;
	if (input % 2 == 1 || input == 2){
		std::cout << "NO";
	} else {
		std::cout << "YES";
	}
}
