// AUTHOR ShenShen shs2016f@bu.edu
#include <string>
#include <vector>
using namespace std;

typedef string BigInt;
typedef vector<int> Poly;

Poly multiply_poly(const Poly &a,const Poly &b)
{	int sizea=a.size();
	int sizeb=b.size();
	int sizec=sizea+sizeb;
	Poly c(sizec,0);
	for (int i=0;i<sizea;i++)
		for (int j=0;j<sizeb;j++)
			c[i+j+1]=a[i]*b[j]+c[i+j+1];
// consider the carry
	for (int k=sizec-1;k>=0;k--){
		if (c[k]>=10){
			c[k-1]=c[k-1]+c[k]/10;
			c[k]=c[k]%10;
			k=sizec;}}
	return c;
}

BigInt multiply_int(const BigInt &a,const BigInt &b)
{	Poly c(a.length(),0);
	Poly d(b.length(),0);
	for (int i=0;i<a.length();i++)
		c[i]=int(a[i])-48;
	for (int j=0;j<b.length();j++)
		d[j]=int(b[j])-48;
	Poly e=multiply_poly(c,d);
	string s(e.size(), 'x');
	for (int k=0;k<e.size();k++)
		s[k]=char(e[k]+48);
	if (s[0]=='0')
		s.erase (s.begin(),s.begin()+1);
	return s;
}

