#include <iostream>
#include <iomanip>

using namespace std;


int main()
{

    // Convert temperatures in Fahrenheit to Celsius

    bool appRunning = true;
    char userInput;

    cout << "+------------------------------+" << endl;
    cout << " Temperature Conversion Program " << endl;
    cout << "+------------------------------+" << endl << endl;

    cout << "Version 1.0.1" << endl << endl;

    cout << "This program converts Celsius to Fahrenheit or Fahrenheit to Celsius" << endl;
    


    while (appRunning)
    {
        float result;
        float temperature;

        cout << endl << "Which temperature scale would you like to convert? " << endl << endl;
        cout << "Type 'F' for Fahrenheit or 'C' for celsius, you can exit by typing 'X': ";
        cin >> userInput;

        if (userInput == 'f' || userInput == 'F')
        {
            cout << endl << "Enter the temperature in Fahrenheit : ";
            cin >> temperature;

            result = (temperature - 32) * (5 / 9);

            cout << endl << temperature << "F is equal to " << fixed << setprecision(2) << result << " degrees C" <<endl;
        }
        else if (userInput == 'c' || userInput == 'C')
        {
            cout << endl << "Enter the temperature in Celsius : ";
            cin >> temperature;

            result = (temperature / 0.55555) + 32;

            cout << endl << temperature << "degrees C is equal to " << fixed << setprecision(2) << result << " degrees F" << endl;
        }
        else if (userInput == 'x' || userInput == 'X')
        {
            cout << "Ending program.." << endl;
            appRunning = false;
        } 
        else
        {
            cout << endl << "Exception: Invalid input " << endl;
        }

    }
    

    return 0;
}