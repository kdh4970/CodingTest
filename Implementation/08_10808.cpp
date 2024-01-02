// 알파벳 개수
#include<bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int num_a = static_cast<int>('a');
    int num_z = static_cast<int>('z');
    int res_arr[num_z-num_a+1] {0};

    string s;
    cin >> s;
    for(auto j : s){
        res_arr[static_cast<int>(j)-num_a]++;
    }
    for(auto _:res_arr)
    {
        cout << _ << ' ';
    }
}