#include <bits/stdc++.h>
using namespace std;
int main(){
	int n, x1, y1, x2 ,y2;
	cin >> n;
	while(n--){
		cin >> x1 >> y1 >> x2 >> y2;
		cout << x1 + (x2 - x1) * 2 << " " << y1 + (y2 - y1) * 2 << endl;
	}
}
	