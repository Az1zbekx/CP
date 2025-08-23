#include <bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin >> n;
	for(int i = 1; i <= 999; i++){
		if(i + i % 100 == n){
			cout << i << " ";
		}
	}
}