#include<bits/stdc++.h>
using namespace std;
int n;
class CComplex {
    private:
        double x, y;
    public:
        CComplex() {
            x = y = 0;
        }
        CComplex(double x) {
            this -> x = x;
            y = 0;
        }
        CComplex(double x, double y) {
            this -> x = x;
            this -> y = y;
        }
        void operator =(const CComplex &E) {
            this -> x = E.x;
            this -> y = E.y;
        }
        CComplex operator +(const CComplex &E) {
            CComplex aux;
            aux.x = this -> x + E.x;
            aux.y = this -> y + E.y;
            return aux;
        }
        CComplex operator -(const CComplex &E) {
            CComplex aux;
            aux.x = this -> x - E.x;
            aux.y = this -> y - E.y;
            return aux;
        }
        CComplex operator *(const CComplex &E) {
            CComplex aux;
            aux.x = this -> x * E.x - this -> y * E.y;
            aux.y = this -> y + E.x + this -> x * E.y;
            return aux;
        }
        CComplex operator /(const CComplex &E) {
            CComplex aux;
            double piv = E.x * E.x + E.y * E.y;
            aux.x = (this -> x * E.x + this -> y * E.y) / piv;
            aux.y = (this -> y * E.x - this -> x * E.y) / piv;
            return aux;
        }
        double operator~() {
            return sqrt(x * x + y * y);
        }
        void operator^(const double pw) {
            CComplex aux;
            aux.x = 1;
            aux.y = 0;
            for(int i = 1; i <= pw; ++i) {
                double piv = aux.x;
                aux.x = this -> x * aux.x - this -> y * aux.y;
                aux.y = this -> x * aux.y + this -> y * piv;
            }
            this -> x = aux.x;
            this -> y = aux.y;
        }
        void print() {
            cout << x << " + " << y << " * i\n";
        }
};

int main()
{
    int n;
	cin >> n;
	CComplex *cn[128];

	for(int i = 1; i <= 2 * n; ++i) {
		double x, y;
        cin >> x >> y;
		cn[i] = new CComplex(x, y);
	}

	CComplex even, odd, ans;

	for (int i = 1; i <= 2 * n - 1; i += 2)
	{
		*cn[i] ^ 3;
		odd = odd + *cn[i];
	}
	for (int i = 2; i <= 2 * n; i += 2)
	{
		*cn[i] ^ 4;
		even = even + *cn[i];
	}

	ans = odd / even;
	ans.print();

	return 0;
}
