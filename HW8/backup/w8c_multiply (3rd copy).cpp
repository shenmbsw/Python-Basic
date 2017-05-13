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

double_matrix double_multiply(const double_matrix& A,const double_matrix& B)
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
    string dtype(argv[1]);
    int M = stoi(argv[2]);
    int N = stoi(argv[3]);
    int L = stoi(argv[4]);
    string file1 (argv[5]);
    string file2 (argv[6]);
    string file3 (argv[7]);

	int_matrix m1 (M,vector<int>(N));
	int_matrix m2 (N,vector<int>(L));
	int_matrix m3 (M,vector<int>(L));

	double_matrix m1_double (M,vector<double>(N));
	double_matrix m2_double (N,vector<double>(L));
	double_matrix m3_double (M,vector<double>(L));


    ifstream thisfile;

if (dtype=="int"){
    thisfile.open(file1);
    for (int i=0; i<M; i++)
        for (int j=0; j<N; j++)
            thisfile >> m1[i][j];
    thisfile.close();

    thisfile.open(file2);

    for (int i=0; i<N; i++)
        for (int j=0; j<L; j++)
            thisfile >> m2[i][j];
    thisfile.close();
    m3 = multiply(m1, m2);

    ofstream mfile;
    mfile.open(file3);

    for (int i=0; i<M; i++)
    {
        for(int j=0; j<L; j++)
            mfile << m3[i][j] << " ";
        mfile<<endl;
    }

    mfile.close();
}

else if (dtype=="double"){
    thisfile.open(file1);
    for (int i=0; i<M; i++)
        for (int j=0; j<N; j++)
            thisfile >> m1_double[i][j];
    thisfile.close();

    thisfile.open(file2);
    for (int i=0; i<N; i++)
        for (int j=0; j<L; j++)
            thisfile >> m2_double[i][j];
    thisfile.close();
    m3_double = double_multiply(m1_double, m2_double);
    ofstream mfile;
    mfile.open(file3);

    for (int i=0; i<M; i++)
    {
        for(int j=0; j<L; j++)
            mfile << m3_double[i][j] << " ";
        mfile<<endl;
    }

    mfile.close();
}


}
