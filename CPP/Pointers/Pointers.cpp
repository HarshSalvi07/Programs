#include<iostream>
using namespace std;
int main()
{
    int num,*pNum;
    num = 10;
    pNum = &num;
    cout << "The value of num is: " << num <<endl;
    cout << "The address of num is: " << pNum <<endl;
    cout << "The value from pointer: " << *pNum << endl;
    return 0;
}
