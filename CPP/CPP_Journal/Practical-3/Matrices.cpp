#include<iostream>
using namespace std;
int main()
{
    int row = 2, column = 2;
    int matrix[row][column];

    for(int i = 0; i < row; i++)
    {
        for(int j = 0; j < column; j++)
        {
            cout<<"Enter the element at a"<<i+1<<j+1<<":";
            cin>>matrix[i][j];
        }
    }
    //Displaying the matrix
    for(int i = 0; i < row; i++)
    {
        for(int j = 0; j < column; j++)
        {
            cout<<matrix[i][j]<<"";
        }
        cout<<endl;
    }
    return 0;
}