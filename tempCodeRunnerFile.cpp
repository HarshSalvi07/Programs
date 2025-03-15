#include<iostream>
using namespace std;
int main()
{
    int row = 2, column = 2;
    int matrix[row][column];

    for(i=1;i<row;i++)
    {
        for(j=1;j<column;j++)
        {
            cout<<"Enter the element at pos a"<<i+1<<j+1<<":";
            cin>>matrix[i][j];
        }
    }

    for(i=1;i<row;i++)
    {
        for(j=1;j<column;j++)
        {
            cout<<matrix[i][j]<<"";
        }
        cout<<endl;
    }
    return 0;
}