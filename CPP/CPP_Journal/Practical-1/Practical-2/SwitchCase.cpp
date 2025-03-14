#include<iostream>
using namespace std;
int main()
{
    int day = 1;
    cout<<"Select a number from 1-7 for day of the week: ";
    cin>>day;

    while(day>7 | day<0)
    {
        cout<<"Invalid input please select a number between 1-7 only: ";
        cin>>day;
    }
    switch(day)
    {
        case 1:
            cout<<"Monday";
            break;
        case 2:
            cout<<"Tuesday";
            break;
        case 3:
            cout<<"Wednesday";
            break;
        case 4:
            cout<<"Thursday";
            break;
        case 5:
            cout<<"Friday";
            break;
        case 6:
            cout<<"Saturday";
            break;
        case 7:
            cout<<"Sunday";
            break;
        default:
            break;
    }
    return 0;
}