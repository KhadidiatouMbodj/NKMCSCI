//Name:  Ndeye Khadidiatou Mbodj
//Email:  NDEYEKHADIDIATOU.mbodj48@myhunter.cuny.edu
//Date:  04/22/2024
//My program in C++

#include <iostream>
using namespace std;
int main()
{
    int year;
    cout<< "Enter a year:";
    cin>> year;
    while (year>2018 )
    {
        cout<< "Year must be 2018 or earlier\n";
        cout<< "Enter a year:";
        cin>> year;
    }
    cout<< "You entered:"<<year;
   
    return 0;
    
}

