#include<iostream>
#include<cstdlib>
#include<time.h>
#include<cmath>

using namespace std;

/* Functions */

void menu(){
    cout << "      Today's Menu" <<endl;
    cout << "-------------------------" <<endl;
    cout << "1.Generate 'n' number of Random Numbers" << endl;
    cout << "2.Factorization" << endl;
    cout << "3.Leap Year Testing" << endl;
    cout << "4.ASCII Conversion" <<endl;
    cout << "5.Prime Number Detection" <<endl;
    cout << "6.Armstrong Number Detection" <<endl;
    cout << "Exit(0)" << endl;
    cout << "--------------------------" << endl;
}

void randomNumber(int n){

    srand(time(NULL)); //Using system time which changes constantly

    for(int i=1;i<=n;i++){
        cout<< rand()<< endl;
    }
    cout << "System Time : " << time(NULL) << endl;
}

void factorization(int n){
  cout << "Factors are 1|";
  for(int i = 2; i<=sqrt(n);i++){
      if(n % i == 0){
        cout << i << "|";
      }
  }
  cout <<""<<endl;
}

void leapYear(int year){

     if(year%4 == 0){
        if(year%100 == 0){
            if(year%400 == 0){
                cout << "Leap year"<<endl;
            }
            else{
                cout << "NOT a leap year" << endl;
            }
        }
        else{
            cout << "Leap year"<<endl;
        }

     }
     else{
        cout << "NOT a leap year" << endl;
     }
}

void asciiConverter(char ch){

    int ch1 = (int)ch - 32;
    cout << (char)ch1 << "(" << ch1 <<")" << endl;
}

void isPrime(int n){

  for(int i = 2; i<=sqrt(n);i++){
      if(n % i == 0){
        cout <<"Not Prime"<<endl;
        break;
      }
      else{
        cout <<"Prime"<<endl;
        break;
      }
  }
  cout <<""<<endl;
}

void isArmstrong(int n){
  int digit{0};
  int sum {0};
  int counter {0};
  int n_temp {n};

    while(n_temp>0){
     n_temp = n_temp/10;
     counter++;
    }

     n_temp = n;

    while(n_temp>0){
     digit = n_temp % 10;
     n_temp = n_temp / 10;
     sum = sum + pow(digit, counter);;
    }

   if(sum == n){
     cout <<"Armstrong"<<endl;
   }
   else{
     cout <<"Not Armstrong"<<endl;
   }

  cout <<""<<endl;
}

void msg(){
   cout << "Good Bye, Arka Dear..." << endl;
}

int main()
{
    char ans {'y'};

 while(ans == 'y'){   // infinity loop

    int option {};
    int n {};
    char ch {};

    menu();    // Call to the menu

    cout << "Enter your option =  ";
    cin >> option;

    switch(option){

        case 1:  cout << "Enter n = ";
                 cin >> n;
                 randomNumber(n);
                 break;

        case 2:  cout << "Enter a number = ";
                 cin >> n;
                 factorization(n);
                 break;

        case 3:  cout << "Enter a year = ";
                 cin >> n;
                 leapYear(n);
                 break;

        case 4:  cout << "Enter a small alphabet = ";
                 cin >> ch;
                 asciiConverter(ch);
                 break;

        case 5:  cout << "Enter a number = ";
                 cin >> n;
                 isPrime(n);
                 break;

        case 6:  cout << "Enter a number = ";
                 cin >> n;
                 isArmstrong(n);
                 break;

        case 0:  ans = 'N';
                 cout << "Exiting... ";
                 msg();
                 break;

        default: cout << "Invalid input ";
                 ans = 'N';
                 cout << "Exiting... ";
                 break;
    }

            jump:cout << ""<<endl;
            if (ans !='N'){
             cout << "Do you want to continue ??? (y/N) = ";
             cin >> ans;

            if(ans == 'y'){
              continue;
             }
            else if(ans == 'N'){
              msg();
              break;
             }
            else{
              cout << "Please type valid input ";
              goto jump;
            }
        }
   }
    return 0;
}
