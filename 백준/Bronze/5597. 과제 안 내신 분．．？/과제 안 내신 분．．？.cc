#include <iostream>

using namespace std;


int main() {
    int stu[31] = { 0, };

    int did;

    for (int i = 0; i < 28; i++) {
        cin >> did;
        stu[did] = 1;
    }

    for (int i = 1; i <= 30; i++) {
        if (!(stu[i])) {
            cout << i <<endl;
        }
    }

    return 0;
}