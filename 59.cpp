//My program in C++

#include <iostream>
using namespace std;

#include <iostream>
using namespace std;

int main() 
{

    int b, x,num;
    cout << "Enter number between -31 and 31: ";
    cin >> num;
   
    if (num<0)
    {
        cout<< "1";
        x=32+num;
    }   
   
    else if (num>=0)
    {
        cout<<"0";
        x=num;
    }
   
    b=16;
    
    while(b>0.5)
    {
     
        if (x >= b)
        {
            cout<< "1";
        }
       
        else if (x < b)
        {
            cout<< "0";
        }
       
        x=x % b;
       
        b=b/2;
    }
    cout<< " \n";
}
