#include <bits/stdc++.h>

int main(){
    
    std::string S;
    std::cin >> S;
    if(S[0] >= 'A' && S[0] <= 'Z'){
        if(S[S.size() - 1] >= 'A' && S[S.size() - 1] <= 'Z'){
            if(S[1] >= '1' && S[1] <= '9'){
                int store = 0;
                for(int i = 2; i <= 6; i++){
                    if(S[i] >= '0' && S[i] <= '9'){
                        store += 1;
                    }
                }
                if(store == 5){
                    std::cout << "Yes" << std::endl;
                    return 0;
                }
            }
            
           
        }
    }
    std::cout << "No" << std::endl;

    return 0;
}