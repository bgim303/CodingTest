#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int answer;
    if(num_list.size() >= 11) {
        answer = 0; // initialize to 0 for summing
        for(int i = 0; i < num_list.size(); i++) {
            answer += num_list[i];
        }
    }
    else {
        answer = 1; // initialize to 1 for multiplying
        for(int i = 0; i < num_list.size(); i++) {
            answer *= num_list[i];
        }
    }
    return answer;
}