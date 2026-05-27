#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, Q;  // number of arrays, number of queries   
    cin >> N >> Q;

    vector<int> arrays[N];
    int results[Q];

    int k = 0;

    for (int i = 0; i < N; i++) {
        cin >> k;
        for (int j = 0; j < k; j++) {
            int a;
            cin >> a;
            arrays[i].push_back(a);
        }
    }

    for (int i = 0; i < Q; i++) {
        int index_i, index_j;
        cin >> index_i >> index_j;
        cout << arrays[index_i][index_j];
    }

    return 0;
}