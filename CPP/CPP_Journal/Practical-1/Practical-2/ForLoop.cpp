#include<iostream>
using namespace std;
class Sum
{
    public:
    int num,sum=0,squareSum=0;
    void read()
    {
        cout<<"Enter the value of num: ";
        cin>>num;
    }
    void compute()
    {
        for(int i=1;i <= num;i++)
        {
            sum += i;
        }
        for(int i=1;i <= num;i++)
        {
            squareSum += i*i;
        }
    }
    void display()
    {
        cout<<"The value of sum till "<<num<<" is: "<<sum<<endl;
        cout<<"The value of square of sum till "<<num<<" is: "<<squareSum<<endl;
    }
};
int main()
{
    Sum s;
    s.read();
    s.compute();
    s.display();
}