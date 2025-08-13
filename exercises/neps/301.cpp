#include <iostream>
#define MAXN 100010
using namespace std;


int parents[MAXN];

int find(int x) {
    if (parents[x] == x) {
        return x;
    }

    return parents[x] = find(parents[x]);
}


int join(int x, int y) {
    x = find(x);
    y = find(y);

    if (x == y) {
        return;
    }

    parents[x] = y;
}


int main(){
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        parents[i] = i;
    }

    for (int i = 0; i < M; i++) {
        int x, y;
        cin >> x >> y;
        join(x - 1, y - 1);
    }

    int count = 0;
    for (int i = 0; i < N; i++){
        if (parents[i] == i) count++;      
    }

    cout << count << endl;
}