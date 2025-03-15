#include<iostream>
using namespace std;
class Salary
{
    protected:
    double salary = 60000;
};
class Programmer: public Salary
{
    protected:
    string Name = "Harsh";
    double bonus = 6000;

    public:
    void display()
    {
        cout<<"Name of the programmer: "<<Name<<endl;
        cout<<"Base salary: "<<salary<<endl;
        cout<<"Bonus: "<<bonus<<endl;
        cout<<"Gross salary: "<<salary+bonus<<endl;
    }
};
int main()
{
    Programmer p;
    p.display();
    return 0;
}
