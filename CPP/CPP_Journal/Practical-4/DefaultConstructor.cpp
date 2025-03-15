#include<iostream>
using namespace std;
class Student
{
    protected:
        string Name,Stream;
        int Roll_No,Age;
    public:
        Student()
        {
            cout<<"Enter your name: ";
            cin>>Name;
            cout<<"Enter your stream: ";
            cin>>Stream;
            cout<<"Enter your roll-no: ";
            cin>>Roll_No;
            cout<<"Enter your age: ";
            cin>>Age;
        }
        void display()
        {
            cout<<"Name: "<<Name<<endl;
            cout<<"Stream: "<<Stream<<endl;
            cout<<"Roll No: "<<Roll_No<<endl;
            cout<<"Age: "<<Age<<endl;
        }
};
int main()
{
Student s;
s.display();
return 0;
}