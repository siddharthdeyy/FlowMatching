#include<iostream>

using namespace std;

int main(){
    int t;
    cin>>t;
    int result[t];
    for(int j = 0; j<t; j++){
        int n, x;
        cin>>n>>x;
        int a[n];
        for(int i=0; i<n; i++){
            cin>>a[i];
        }
        int b[n+1];
        b[0] = a[0];
        b[n] = 2*(x-a[n-1]);
        for(int i=1;i<n;i++){
            b[i] = a[i] - a[i-1];
        }
        result[j] = b[0];
        for(int i = 1; i<=n;i++){
            if(b[i]>result[j]){
                result[j] = b[i];
            }
        }
    }
    for(int j=0; j<t; j++){
        cout<<result[j]<<endl;
    }
}

