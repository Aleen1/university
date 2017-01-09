#include<bits/stdc++.h>
using namespace std;

struct Node {
	Node *l[28];
	int number;
	int used;
};

class Trie {
private:
	Node *t;
public:
	Trie() {
        t = new Node;
        memset(t, 0, sizeof(Node));
    }

    void add(const char *c){
        Node *q = t;
        int i = 0;
        while (c[i] != '\0')
        {
            if (!q->l[c[i] - 'a'])
            {
                q->l[c[i] - 'a'] = new Node;
                memset(q->l[c[i] - 'a'], 0, sizeof(Node));
            }
            q = q->l[c[i] - 'a'];
            ++i;
        }
        q->number += 1;
    }

	void remove(const char *c) {
        Node *q = t;
        int i = 0;
        while (c[i] != '\0')
        {
            if (!q->l[c[i] - 'a'])
                throw "Cuvantul nu exista in DEX.\n";
            q = q->l[c[i] - 'a'];
            ++i;
        }
        q->used++;
        if (q->used > q->number)
            throw "Cuvantul a mai fost folosit.\n";
    }

	void find(const char *c) {
        Node *v[21], *q = t;
        int i = 0, j = 0;
        v[0] = t;
        while (c[i] != '\0') {
            if (!q->l[c[i] - 'a'])
                throw "Cuvantul nu exista in DEX.\n";
            v[i + 1] = q->l[c[i] - 'a'];

            q = q->l[c[i] - 'a'];
            ++i;
        }
        v[i]->number -= 1;

        while (i > 0 && v[i]->number == 0) {
            for (j = 0; j < 27; ++j)
                if (v[i]->l[j] != 0)
                    break;
            if (j == 27)
            {
                delete v[i];
                v[i - 1]->l[c[i - 1] - 'a'] = 0;
                --i;
            }
            else
                i = 0;
        }
    }

	int print(const char *c) {
        Node *q = t;
        int i = 0;
        while (c[i] != '\0')
        {
            if (!q->l[c[i] - 'a'])
                return 0;
            q = q->l[c[i] - 'a'];
            ++i;
        }
        return q->number;
    }

	int length_com_pref(const char *c) {
        Node *q = t;
        int i = 0;
        while (c[i] != '\0')
        {
            if (!q->l[c[i] - 'a'])
                return i;
            q = q->l[c[i] - 'a'];
            ++i;
        }
        return i;
    }
};

void check(char word[],int letter1,int letter2)
{
	int l = strlen(word);
	if (l < 2)
		throw "Lungimea este prea mica\n";

	if (letter1 != 0 && letter2 != 0)
		if (word[0] != letter1 || word[1] != letter2)
			throw "Cuvantul introdus este gresit.\n";
}

ifstream fin("fazan.in");
Trie trie;
char dex[111], player1[111], player2[111], word[111], letter1, letter2;
int player, len;
bool quit = false;

int main() {
	while (fin >> dex) {
		trie.add(dex);
	}

	cout << "1st player: ";
	cin >> player1;
	cout << "2nd player: ";
	cin >> player2;

	do {
		if (player) {
			cout << player1 << ": ";
			cin >> word;
		} else {
			cout << player2 << ": ";
			cin >> word;
		}

		if (strcmp(word, "!") == 0)
			quit = true;

		if (quit == false) {
			try {
				check(word, letter1, letter2);
				trie.find(word);
                player ^= 1;
				len = strlen(word);
				letter1 = word[len - 2];
				letter2 = word[len - 1];
			}
			catch (const char* msg) {
				cout << msg;
			}
		}
	} while (quit == false);

	return 0;
}
