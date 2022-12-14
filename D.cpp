#include <bits.stdc++.h>
\using namespace std;

int counter = 0;

void Combination(vector<int> v, int n, int r, int vIndex, vector<int> temp, int tempIndex) {
    temp.at(tempIndex) = vIndex;
    if (tempIndex < r - 1) return Combination(v, n, r, vIndex + 1, temp, tempIndex + 1);
    for (int i = 0; i < temp.size(); i++) {
        cout << temp.at(i) << ",";
    }
    cout << endl;
    counter += 1;
    if (temp.at(0) == n - r) return;
    if (vIndex == v.size() - 1) {
        for (int i = r - 1, j = n - 1; i >= 0; i--, j--) {
            if (temp[i] < j) return Combination(v, n, r, temp.at(i) + 1, temp, i);
        }
    }
    return Combination(v, n, r, vIndex + 1, temp, tempIndex);
}
int main() {
    int N, K, D;
    cin >> N >> K >> D;
    int a;
    for(int i = 1; i <= N; i++){
        cin >> a;
        test.push_back(a);
    }
    //vector<int> test = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    vector<int> temp(K);
    Combination(test, test.size(), 5, 0, temp, 0);
    cout << counter << endl;
    return 0;
}