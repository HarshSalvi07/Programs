#include<iostream>
using namespace std;
class Polygon
{
    protected:
    double height,width;

    public:
    void read(double h, double w)
    {
        height = h;
        width = w;
    }
};

class Rectangle: public Polygon
{
    public:
    double area()
    {
        return height * width;
    }
};

class Triangle: public Polygon
{
    public:
    double area()
    {
        return 0.5 * height * width;
    }
};
class Output: public Triangle, public Rectangle
{
    protected:
    int choice;

    public:
    Output(int c)
    {
        choice = c;
    }
    void display()
    {
        switch(choice)
        {
            case 1:
            Triangle::read(12,14);
            cout<<"The area of triangle is: "<<Triangle::area()<<endl;
            break;

            case 2:
            Rectangle::read(12,14);
            cout<<"The area of rectangle is: "<<Rectangle::area()<<endl;
            break;

            default:
            break;
        }
    }
};

int main()
{
    int c;
    cout<<"---------Area Calculator--------------"<<endl;
    cout<<"1-Triangle & 2-Rectangle"<<endl;
    cout<<"Enter a choice: ";
    cin>>c;

    while(c <= 0 || c > 2)
    {
        cout<<"Enter a valid choice: ";
        cin>>c;
    }
    Output o(c);
    o.display();

    return 0;
}