#include<bits/stdc++.h>
using namespace std;

class DEX;

class synonym
{
private:
    set<string> S;

public:
    friend DEX;

    void add_synonym(string synonym)
    {
        S.insert(synonym);
    }

    void print_words()
    {
        for(auto it = S.begin(); it != S.end(); ++it)
            cout << *it << ' ';
        cout << '\n';
    }

};

class DEX
{
private:
    unordered_map<string, synonym> MP;
public:

    void add_syn(string word, string synonym)
    {
        MP[word].add_synonym(synonym);
    }

    void print_list(string word)
    {
        auto it = MP.find(word);
        if(it != MP.end())
        {
            it->second.print_words();
        }
        else
        {
            cout << "The word you are looking for does not exist.\n";
        }
    }

};

int main()
{
    DEX dex;

    dex.add_syn("gabiTorco", "prost");
    dex.add_syn("gabi", "fraIEr");
    dex.add_syn("aleen", "zeu");

    dex.print_list("gabiTorco");
    dex.print_list("alin");
    dex.print_list("aleen");


    return 0;
}
