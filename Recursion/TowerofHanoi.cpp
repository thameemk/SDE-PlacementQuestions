// View Full Question
// https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

#include<iostream>
using namespace std;

void towerOfHanoi(int n, char A = 'A', char B = 'B', char C = 'C') {
	if (n == 1) {
		cout << "Move disk 1 from rod " << A <<
		     " to rod " << C << endl;
		return;
	}

	towerOfHanoi(n - 1, A, C, B);
	cout << "Move disk " << n << " from rod " << A <<
	     " to rod " << C << endl;
	towerOfHanoi(n - 1, B, A, C);
}

int main()
{
    towerOfHanoi(4, 'A', 'C', 'B');
    return 0;
}