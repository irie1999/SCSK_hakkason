#include <bits/stdc++.h>

int main(){

    long long int start_music = 0, end_music = 0;
    long long int N, T;
    std::cin >> N >> T;
    long long int A[N + 1];
    long long int sum = 0;
    for(long long int i = 1; i <= N; i++){
        std::cin >> A[i];
        sum += A[i];
    }
    long long int store_loop = 0;

    long long int new_T = T % sum;
    
    for(long long int i = 1; i <= N; i++){
        end_music += A[i];
        if(new_T <= end_music && new_T >= start_music){
            std::cout << i << " " << new_T - start_music << std::endl;
            return 0;
        }

        start_music += A[i];
    }


    // while(1){
    //     store_loop += 1;
    //     if(sum * store_loop >= T){
    //         start_music = sum * (store_loop - 1); 
           
    //         for(long long int i = 1; i <= N; i++){
    //             end_music += A[i];
    //             if(T <= end_music && T >= start_music){
    //                 std::cout << i << " " << T - start_music << std::endl;
    //                 return 0;
    //             }


    //             start_music += A[i];
    //         }
    //     }
        
    // }

    return 0;
}