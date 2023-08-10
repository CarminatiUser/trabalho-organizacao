#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream inputFile("input.txt");

    if (!inputFile.is_open()) {
        cerr << "Erro ao abrir o arquivo de entrada." << endl;
        return 1;
    }

    string binaryString;
    string line;
    while (getline(inputFile, line)) {
        binaryString += line;
    }

    inputFile.close();

    int groupSize = 7;
    for (size_t i = 0; i < binaryString.length(); i += groupSize) {
        string group = binaryString.substr(i, groupSize);
        cout << group << endl;
    }

    system("pause");

    return 0;
}
