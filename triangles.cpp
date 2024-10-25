//Name:  Ndeye Khadidiatou Mbodj
//Email:  NDEYEKHADIDIATOU.mbodj48@myhunter.cuny.edu
//Date:  04/22/2024
//My program in C++

#include <iostream>
using namespace std;
int main()
{
    int lines;
	cout << "Enter a number: ";
	cin >> lines;
	for(int i = 1; i <= lines; i++) {
		for(int j = 0; j < i; j++){
			cout << "*";
		}
		cout << "\n";
	}
}