#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <map>
#include <utility>
using namespace std;

int main()
{
	string word;									//used to store words as they are read from the file
	string letters,tempLetters;					    //letters holds the string of characters entered on the command line. TempLetters holds a copy of letters
	string firstStr, secondStr;						//variables hold first hand second parts of strings generated from letters
	vector<string> firstWords, secondWords; 		//words lists generated from letters based on word length
	unsigned int wordLength;						//length for firstWord
	map<int, vector<string>> wordsoflength;			//stores words from file by word size and alphabetically for each size
	vector<pair<string,string>> wordsFound;	        //stores the results
	pair <string,string>  wordsfnd1;
	pair <string,string>  wordsfnd2;


    ifstream wordsFile;
	  wordsFile.open("small_wordlist.txt");

	  while(wordsFile >> word) wordsoflength[word.size()].push_back(word);       //Read contents of file word by word into map

	  wordsFile.close();		                                             //close file

	for (int i=0; i <wordsoflength[5].size(); i++)	
		cout<<wordsoflength[5][i]<<endl;

	return 0;
}
