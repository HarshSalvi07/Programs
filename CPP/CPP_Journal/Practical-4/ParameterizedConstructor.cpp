#include<iostream>
using namespace std;
class Circle
{
    protected:
        double Radius;
    
    public:
        Circle(double r)
        {
            Radius = r;
        }
        void displayCircumference()
        {
            cout<<"The circumference of the circle is: "<<2 * 3.14 *Radius<<endl;
        }
        void displayArea()
        {
            cout<<"The area of the circle is: "<<3.14*Radius*Radius<<endl;
        }
};
int main()
{
    int r = 0;
    cout<<"Enter the value of radius: ";
    cin>>r;

    while(r < 0)
    {
    cout<<"Please enter a valid radius: ";
    cin>>r;
    }
    Circle c(r);
    c.displayCircumference();
    c.displayArea();
    return 0;
}