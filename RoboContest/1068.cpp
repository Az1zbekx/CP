#include <bits/stdc++.h>
using namespace std;
int main(){
	string a, b;
	cin >> a >> b;
	if(a.back() == 'v') swap(a, b);
	cout << a << " " << b;
}
	