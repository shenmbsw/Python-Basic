// AUTHOR ShenShen shs2016f@bu.edu
#include <vector>
using namespace std;

typedef vector<double> Poly;

// Add two polynomials, returning the result
Poly add_poly(const Poly &a,const Poly &b)
{	int sizea=a.size();
	int sizeb=b.size();
	
	if (sizea<=sizeb){
		Poly c=b;
		for (int i=0;i<sizea;i++)
			c[i]=c[i]+a[i];
	return c;}
	
	else{
		Poly c=a;
		for (int i=0;i<sizeb;i++)
			c[i]=c[i]+b[i];	
	return c;}
}


Poly multiply_poly(const Poly &a,const Poly &b)
{	int sizea=a.size();
	int sizeb=b.size();
	int sizec=sizea+sizeb-1;
	Poly c(sizec,0);
	for (int i=0;i<sizeb;i++)
		for (int j=0;j<sizea;j++)
			c[i+j]=c[i+j]+a[j]*b[i];
	return c;
}

