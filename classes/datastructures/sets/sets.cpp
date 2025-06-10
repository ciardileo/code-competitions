#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

int main(){
    set<int> orderedset = {2, 3, 4};  // ordered set have index, so we can iterate over them with begin() and advance()
    unordered_set<int> unorderedset = {2, 3, 4}; // normal set

    unorderedset.insert(4);
    cout << unorderedset.size() << endl;
    cout << unorderedset.count(2) << endl;

    return 0;
}