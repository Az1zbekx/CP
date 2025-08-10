#include <bits/stdc++.h>
using namespace std;
int main(){
	long long n, m, k = 0;
	cin >> n >> m;
	for(long long i = n; i < m + 1; i++){
		if(i % 3 == 0 && i % 7 != 0) k += i;
	}
	cout << k;
}