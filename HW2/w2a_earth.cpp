// AUTHOR ShenShen shs2016f@bu.edu
// AUTHOR Patrick Dyer pddyer21@bu.edu 

#include <iostream>
#include <cmath>
using namespace std;

int main(){
double mass_earth=5.972e27; 		 //unit:g
double neu_add_pro=mass_earth*6.02e23;   //the whole number of neu and pro
double EperP1=0.5;			 //E per P means electron per particle
double EperP2=0.4;
double EperP3=1;

double a1=neu_add_pro*EperP1;		//how much bits
double a2=neu_add_pro*EperP2;
double a3=neu_add_pro*EperP3;


double b1=a1/pow(2,43);
double b2=a2/pow(2,43);
double b3=a3/pow(2,43);

cout<<b1<<endl;
cout<<b2<<endl;
cout<<b3<<endl;
}

