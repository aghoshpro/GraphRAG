#include<iostream>
#include<cstdlib>
#include<time.h>
#include<cmath>
#include <chrono>
#include<windows.h>

using namespace std;

/* ****** F(x) *************************************************************************************** */

void menu(){
    cout << "      Today's Menu" <<endl;
    cout << "-------------------------" <<endl;
    cout << "1.Generate 'n' number of Random Numbers" << endl;
    cout << "2.Factorization" << endl;
    cout << "3.Leap Year Testing" << endl;
    cout << "4.ASCII Conversion" <<endl;
    cout << "5.Prime Number Detection" <<endl;
    cout << "6.Armstrong Number Detection" <<endl;
    cout << "7.Colour Matrix" <<endl;
    cout << "8.Change Text Color" <<endl;
    cout << "9.Inverse Background" <<endl;
    cout << "10.Infinite Colour Waterfall" <<endl;
    cout << "Exit(0)" << endl;
    cout << "--------------------------" << endl;
}

void changeBG(){
        system("Color F0");
    /*
    1	Blue	9	Light Blue
    2	Green	0	Black
    3	Aqua	A	Light Green
    4	Red 	B	Light Aqua
    5	Purple	C	Light Red
    6	Yellow	D	Light Purple
    7	White	E	Light Yellow
    8	Gray	F	Bright White

    B for background Color(Light Aqua)
    5 for text color(Purple)
    */
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

void Color(int color){
 SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), color);
 //COLORS LIST
//1: Blue
//2: Green
//3: Cyan
//4: Red
//5: Purple
//6: Yellow (Dark)
//7: Default white
//8: Gray/Grey
//9: Bright blue
//10: Bright green
//11: Bright cyan
//12: Bright red
//13: Pink/Magenta
//14: Yellow
//15: Bright white
//Numbers after 15 include background colours
}

void buildMatrix(int rows, int cols){

    int M[rows][cols] = {0};

    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            M[i][j] = rand()%100; // range: 0 to 100
        }
    }
    cout << endl;
    cout << "     Generated Matrix     " << endl;
    cout << "-------------------------" << endl;

    for(int i=0;i<rows;++i){
        for(int j=0;j<cols;++j){
            //Color(rand()%14);
            //changeBG();
            cout << M[i][j] << " ";
        }
     cout << endl;
    }

     cout << endl;

    for(int i=0;i<rows;++i){
        for(int j=0;j<cols;++j){
           Color(rand()%14);
           cout << char(219)<<char(219);
        }
     cout << endl;
    }
}

void colorWaterfall(){

 while(1){
     for(int i=0;i<10;++i){
        for(int j=0;j<10;++j){
           Color(rand()%14);
           cout << char(219)<<char(219);
        }
     cout << flush;
    }
  }
}

void msg(){
   cout << "Good Bye, Arka Dear..." << endl;
}

/* ****** END of F(x) ********************************************************************************** */


int main()
{
    char ans {'y'};

 while(ans == 'y'){   // infinity loop

    int option {};
    int n {};
    int rows, cols;
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

        case 7:  cout << "Rows = ";
                 cin >> rows;
                 cout << "Columns = ";
                 cin >> cols;
                 buildMatrix(rows, cols);
                 break;

        case 8:  cout << "Enter a number (0-15) = ";
                 cin >> n;
                 Color(n);
                 break;

        case 9:  changeBG();
                 break;

        case 10: colorWaterfall();
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
