// AUTHOR shenshen shs2016f@bu.edu
// AUTHOR You Han yhan94@bu.edu

#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

typedef vector< vector<int> > int_matrix;
typedef vector< vector<double> > double_matrix;


int_matrix multiply(const int_matrix& A,const int_matrix& B)
{

 int M = A.size();
 int N = A[0].size();
 int L = B[0].size();

 int_matrix c(M,vector<int>(L));

 for (int i=0;i<M;i++)
    for (int j=0;j<L;j++)
        for (int k=0;k<N;k++)
            c[i][j] += A[i][k] * B[k][j];

 return c;
}

double_matrix multiply(const double_matrix& A,const double_matrix& B)
{

 int M = A.size();
 int N = A[0].size();
 int L = B[0].size();

 double_matrix c(M,vector<double>(L));

 for (int i=0;i<M;i++)
    for (int j=0;j<L;j++)
        for (int k=0;k<N;k++)
            c[i][j] += A[i][k] * B[k][j];
 return c;
}


int main(int argc, char const *argv[])
{
        int M,N,L;
        int offset=0;

        try
        { 	if (argc==8){
    	        M = atoi(argv[2]);
    	        N = atoi(argv[3]);
    	        L = atoi(argv[4]);
    	        offset=2;}

    		else if(argc==6)
    	            M = N = L = atoi(argv[2]);

		else
		{
	      	    return 1;}
            }
            catch (...)
            {
		return 1;
            }
    if(M<=0|N<=0|L<=0)
	return 1;

    int_matrix m1 (M,vector<int>(N));
    int_matrix m2 (N,vector<int>(L));
    int_matrix m3 (M,vector<int>(L));

    double_matrix m1_double (M,vector<double>(N));
    double_matrix m2_double (N,vector<double>(L));
    double_matrix m3_double (M,vector<double>(L));

    int a;	
    int flag1;


ifstream thisfile;

if (string(argv[1])=="int"){
    try
    {
    	thisfile.open(argv[offset+3]);
    	for (int i=0; i<M; i++){
   	    for (int j=0; j<N; j++){
    		thisfile >> m1[i][j];}}
	flag1=thisfile.eof();
	thisfile >> a;
	if (flag1!=0|thisfile.eof()!=1)
		return 3;
    	thisfile.close();

        thisfile.open(argv[offset+4]);
        for (int i=0; i<N; i++){
            for (int j=0; j<L; j++)
                thisfile >> m2[i][j];}
	flag1=thisfile.eof();
	thisfile >> a;
	if (flag1!=0|thisfile.eof()!=1)
		return 3;
        thisfile.close();
    }
    catch (...)
        {
            return 2;
        }
    try
    {
        m3 = multiply(m1, m2);
    }
    catch(...)
        {
	     return 3;
        }

    ofstream mfile;

	if (string(argv[offset+5])=="UNREADABLE")
	    return 4;


    try
    {
        mfile.open(argv[offset+5]);
        for (int i=0; i<M; i++)
        {
            for(int j=0; j<L; j++)
                mfile << m3[i][j] << " ";
            mfile<<endl;
        }
        mfile.close();
    }
        catch (...)
        {
            return 4;
        }


    return 0;
}

if (string(argv[1])=="double"){
    try
    {
    	thisfile.open(argv[offset+3]);
    	for (int i=0; i<M; i++){
   	    for (int j=0; j<N; j++){
    		thisfile >> m1_double[i][j];}}
	flag1=thisfile.eof();
	thisfile >> a;
	if (flag1!=0|thisfile.eof()!=1)
		return 3;
    	thisfile.close();

        thisfile.open(argv[offset+4]);
        for (int i=0; i<N; i++){
            for (int j=0; j<L; j++)
                thisfile >> m2_double[i][j];}
	flag1=thisfile.eof();
	thisfile >> a;
	if (flag1!=0|thisfile.eof()!=1)
		return 3;
        thisfile.close();
    }
    catch (...)
        {
	    
            return 2;
        }
    try
    {
        m3_double = multiply(m1_double, m2_double);
    }
    catch(...)
        {
	     
	     return 3;
        }

    ofstream mfile;

	if (string(argv[offset+5])=="UNREADABLE")
	    return 4;

    try
    {
        mfile.open(argv[offset+5]);
	
        for (int i=0; i<M; i++)
        {
            for(int j=0; j<L; j++)
                mfile << m3_double[i][j] << " ";
            mfile<<endl;
        }
        mfile.close();
    }
        catch (...)
        {   
            return 4;
        }
    
    return 0;
}



else
    
    return 1;
}
