#include <bits/stdc++.h>
using namespace std;
int main(){
	int n, k;
	cin >> n >> k;
	if(n % k) cout << n / k + 1;
	else cout << n / k;
}
	