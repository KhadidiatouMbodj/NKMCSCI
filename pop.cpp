//Date:  04/22/2024
//My program in C++

#include <iostream>
using namespace std;

int main() 
{
    int numYears;
    cout << "Enter number of years: ";
    cin >> numYears;
    double p = 325.7; 
    double B = 12.4/1000;
    double D = 8.4/1000;
    
    for(int i = 2017; i < 2017+numYears; i++) {
        //print current population
        cout << "Year\t" << i << "\t"<< p << endl;
        //calculate next year's expected population
        p = p + B*p - D*p;
    }
}
