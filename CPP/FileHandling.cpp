#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    char msg[20];
    ofstream o;
    o.open("test1.txt",ios::out);
    o<<"HelloFriends!!!"<<endl;
    o<<"Byeeeeee!!!"<<endl;
    o.close();
    ifstream i;
    i.open("test1.txt",ios::in);
    i>>msg;
    cout<<msg<<endl;
    i>>msg;
    cout<<msg<<endl;
    i.close();
    return 0;
}