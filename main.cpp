#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
    string foods[] = {"Hamburger", "Hotdog", "BBQ Wings", "Fries"};

    int count = 1;

    for(string food_item : foods)
    {
        

        cout << "Food item " << count << ": " << food_item << endl;
        count++;
    }

    return 0;
}