#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string letter) {
    string res ="";
    for (int i = 0; i< my_string.size();i++){
        if(my_string[i] != letter[0]){
            res += my_string[i];
        }
    }
    return res;
}