#include<iostream>
using namespace std;
class Circle
{
    public:
    double radius,circumference,area;
    void read()
    {
        cout<<"Enter the radius of the circle: ";
        cin>>radius;
    }
    void compute()
    {
        circumference = 2 * 3.14 * radius;
        area = 3.14 * radius * radius;
    }
    void display()
    {
        cout<<"The circumference of the circle is: "<<circumference<<endl;
        cout<<"The area of the circle is: "<<area<<endl;
    }
};
int main()
{
    Circle c;
    c.read();
    c.compute();
    c.display();
    return 0;
}