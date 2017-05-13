// AUTHOR ShenShen shs2016f@bu.edu

#include <iostream>
#include <ctime>

using namespace std;

int main()
{
	
	clock_t start_clock,end_clock;
	start_clock = clock(); 
	short unsigned int i = 1;
	while ( i > 0 ) i++;
	end_clock = clock();    
	double t1 = (double)(end_clock-start_clock) / CLOCKS_PER_SEC;

	start_clock = clock();  
	unsigned int j = 1;
	while ( j > 0 ) j++;
	end_clock = clock();    
	double t2 = (double)(end_clock-start_clock) / CLOCKS_PER_SEC;

	long unsigned int k=0;
	k--;
	j--;
	double t3 = t2*k/j;
	
	cout << "short unsigned int time (microseconds):"<< t1*1e6 << endl;
	cout << "unsigned int, time(second)"<<t2 << endl;
	cout << "long unsigned int, time(year)"<<t3/3.1536e7 << endl;
}
