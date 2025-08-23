#include <bits/stdc++.h>
using namespace std;
bool fun(string s, int l, int r){
	for(int i = l; i <= r; i++){
		if(s[i] == '0') return false;
	}
	return true;
}
int main(){
	string s;
	cin >> s;
	int l = s.find('1'), r = s.rfind('1');
	cout << (fun(s, l, r) ? "YES" : "NO");
}