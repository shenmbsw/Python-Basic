// AUTHOR Shen Shen shs2016f@bu.edu
// AUTHOR You Han yhan94@bu.edu
//  Copyright [2016] <ss>

#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <map>

using std ::cout;
using std ::cin;
using std ::string;
using std ::map;
using std ::vector;
using std ::ifstream;

int main(int argc, char const *argv[]) {
    string word;
    string sortword;
    map< int, map< string, vector<string>>> dict;

    ifstream wordsFile;
    wordsFile.open(argv[1]);

    while (wordsFile >> word) {
        sortword = word;
        sort(sortword.begin(), sortword.end());
        dict[word.size()][sortword].push_back(word);
    }
    wordsFile.close();
    while (1) {
        vector<string> result;
        string text;
        string txt;
        int num;

        cin  >>  text  >>  num;
        if (num == 0) {
            return 0;
        } else {
            if (num == text.size()) {
                if (dict.count(num) > 0) {
                    sort(text.begin(), text.end());
                    result = dict[num][text];
                }
            }  else {
            if (dict.count(num) > 0) {
            for (auto& x : dict[num]) {
                int flag = 1;
                for (auto& j : x.first) {
                    string::size_type found = text.find(j);
                    if (found == string::npos) {
                    flag = 0;
                    break;
                    }
                }
                if (flag == 1) {
                    for (auto& y : dict[num][x.first]) {
                        txt = text;
                        for (auto& j : y) {
                            string::size_type found = txt.find(j);
                            if (found != string::npos) {
                                txt.erase(txt.begin() + found);
                            } else {
                                flag = 0;
                                break;}}
                        if (flag ==1) result.push_back(y);
                    } } } } } }

    sort(result.begin(), result.end());
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << '\n';
    }
    cout << '.' << '\n';
    }

    return 0;
}

