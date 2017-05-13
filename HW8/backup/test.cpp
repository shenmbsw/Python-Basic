// AUTHOR shenshen shs2016f@bu.edu

#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

typedef vector< vector<int> > int_matrix;
typedef vector< vector<double> > double_matrix;


const arg_invalid=1;    //the command line arguments are invalid (return code 1)
const file_not_exist=2; //one or more of the input files do not exist (return code 2)
const data_error=3;     //the data in the files does not conform to the expectations. (return code 3)
const can_not_creat=4;  //the result matrix cannot be created (return code 4)
const other_wrong=5;    //If there are cases I have not thought of yet, use return codes 5 and up.


int read_file (int argc, char const *argv[], string& dtype, string& file1, string& file2, string& file3, int& M, int& N, int& L)
int creat_matrix (string filename,const int_matrix& m)
int creat_matrix (string filename,const double_matrix& m)
int multiply(const int_matrix& A,const int_matrix& B,const int_matrix& C)
int multiply(const double_matrix& A,const double_matrix& B,const double_matrix& C)
int write_file (string filename,const int_matrix& m)
int write_file (string filename,const double_matrix& m)

int main(int argc, char const *argv[])
{
    string dtype,file1,file2,file3;
    int M,N,L;
    int error_code=0;
    error_code=read_file(argc,argv[],dtype,file1,file2,file3,M,N,L)

    int_matrix m1 (M,vector<int>(N));
    int_matrix m2 (N,vector<int>(L));
    int_matrix m3 (M,vector<int>(L));

    double_matrix m1_double (M,vector<double>(N));
    double_matrix m2_double (N,vector<double>(L));
    double_matrix m3_double (M,vector<double>(L));

    error_code=creat
    
