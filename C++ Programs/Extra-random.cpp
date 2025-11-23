
#include <iostream>


using namespace std;


int main(int argc, char* argv[])
{
   int max = 100;
   int min = 1;


    srand(time(NULL));

    int randomSeed = (rand() % max) + min;

    if ((randomSeed % 2 == 0))
    {
            cout << "Random number: " << randomSeed;
        
    } 
    else
    {
            cout << "Random number: " << max - randomSeed;
    }
         
    return 0;
}