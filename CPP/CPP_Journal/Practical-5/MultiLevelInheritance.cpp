#include<iostream>
using namespace std;
class Data
{
    protected:
    int P,C,M,B;

    public:
    void read()
    {
        cout<<"Enter the marks obtained in Physics: ";
        cin>>P;
        cout<<"Enter the marks obtained in Chemistry: ";
        cin>>C;
        cout<<"Enter the marks obtained in Maths: ";
        cin>>M;
        cout<<"Enter the marks obtained in Biology: ";
        cin>>B;
    }
};
class Sum: public Data
{
    protected:
    double totalMarks;

    public:
    void sum()
    {
        totalMarks = P+C+M+B;
    }
};
class Percentage: public Sum
{
    protected:
    double percentage;
    public:
    void calculate()
    {
        percentage = (totalMarks/400)*100;
    }
    void display()
    {
        cout<<"-----------Result------------"<<endl;
        cout<<"Physics: "<<P<<endl;
        cout<<"Chemistry: "<<C<<endl;
        cout<<"Maths: "<<M<<endl;
        cout<<"Biology: "<<B<<endl;
        cout<<"Total Marks: "<<totalMarks<<"/400"<<endl;
        cout<<"Percentage Obtained: "<<percentage<<"%"<<endl;
    }
};
int main()
{
    Percentage p;
    p.read();
    p.sum();
    p.calculate();
    p.display();

    return 0;
}