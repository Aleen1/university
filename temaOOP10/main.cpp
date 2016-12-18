#include<bits/stdc++.h>
using namespace std;

class ATM {
    private:
        int cash , plafon;
    public:
        ATM() {
            cash = 0;
            plafon = 5000;
        }
        void withdraw()
        {
            int wanted;
            cin >> wanted;
            try {
                if(cash < wanted) {
                    throw "mai munceste.\n";
                } else {
                    if(wanted > plafon) {
                        throw "nu avem atat.\n";
                    } else {
                        cash -= wanted;
                    }
                }
            }
            catch (const char* message) {
                cout << message;
            }
        }
        void add() {
            int payment;
            cin >> payment;
            cash += payment;
        }
};

int main() {

    ATM BCR;
    BCR.add();
    BCR.withdraw();

    return 0;
}
