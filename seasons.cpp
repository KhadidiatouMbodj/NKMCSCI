//Date:  04/22/2024
//My program in C++

#include <iostream>
using namespace std;
int main()
{
    int month;
    cout<< "Enter a month in number:";
    cin>> month;
    if (month<3 || month>11 )
        cout<< "Happy Winter";
    else if (month>=3 && month<7)
        cout<< "Happy Spring";
    else if (month>=7 && month<9)
        cout<< "Happy Summer";
    else
     cout<< "Happy Fall";
    return 0;
    
}
