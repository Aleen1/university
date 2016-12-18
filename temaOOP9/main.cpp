#include<bits/stdc++.h>
using namespace std;

template <typename T>
void sort (vector<T> &arr) {
	for (int i = 0; i < arr.size(); i++){
		int j = i;
		while (j > 0 && arr[j] < arr[j-1]){
			  T temp = arr[j];
			  arr[j] = arr[j-1];
			  arr[j-1] = temp;
			  j--;
			  }
		}
}

vector<string> names;
int n;

int main() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        string x;
        cin >> x;
        names.push_back(x);
    }

    sort(names);
    for(auto &it : names){
        cout << it << '\n';
    }

    return 0;
}
