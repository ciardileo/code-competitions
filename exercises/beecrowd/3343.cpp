#include <iostream>
#include <vector>
using namespace std;

/* WORKS, BUT EXCEPTS THE TIME LIMIT
while giants:
    for each giant, if he's shorter than the next wall in the vector
        add the wall to a vector
        and change the initial point of walls to its point
*/

int main(){
    // declarations
    int numTitans, wallSize, sizeP, sizeM, sizeG, totalWalls;
    string sequence;
    vector<int> walls;

    // inputs
    cin >> numTitans;
    cin >> wallSize;

    cin >> sequence;

    cin >> sizeP;
    cin >> sizeM;
    cin >> sizeG;

    walls.push_back(wallSize);
    totalWalls ++;

    for (int i = 0; i < numTitans; i++){
        int giant = 0;

        switch (sequence[i]){
        case 'P':
            giant = sizeP;
            break;
        
        case 'M':
            giant = sizeM;
            break;

        case 'G':
            giant = sizeG;
            break;
        }

        for (int j = 0; j < totalWalls; j++){
            if (giant <= walls[j]){
                walls[j] -= giant;
                giant = 0;
                break;
            }
        }

        if (giant != 0){
            walls.push_back(wallSize - giant);
            totalWalls ++;
        }
    }

    cout << totalWalls;

    return 0;
}