#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>
using namespace ::std;

void save_text_to_bits(unordered_map<char,string> hash_map);

int main() {
    ifstream file;
    file.open("C:\\Users\\weron\\OneDrive\\Pulpit\\Kod_huffmana\\prefixes.txt");
    if(file.good()){
        unordered_map<char, string> char_to_prefix_map;
        string prefix;
        char character;
        string get;

        while (file.get(character)) {
            file.ignore(1);
            getline(file, prefix);
            char_to_prefix_map[character] = prefix;
        }
        file.close();
        save_text_to_bits(char_to_prefix_map);
    }
    else{
        cout<<"Cannot open code file";
    }
    return 0;
}


void save_text_to_bits(unordered_map<char,string> hash_map){
    ifstream file;
    file.open("C:\\Users\\weron\\OneDrive\\Pulpit\\Kod_huffmana\\text_file.txt");
    ofstream bit_file("C:\\Users\\weron\\OneDrive\\Pulpit\\Kod_huffmana\\binary_file.bin",ios::binary);
    char sign;
    string prefix_code;
    int counter1=0;
    unsigned char current_byte=0;
    int bit_count=0;
    if(file.good() && bit_file.good()){
        while(file.get(sign)){
            prefix_code=hash_map[sign];
            for(char bit : prefix_code){
                if (bit == '1') {
                    current_byte |= (1 << (7 - bit_count));
                }
                bit_count++;
                if(bit_count==8){
                    counter1+=8;
                    bit_file.write(reinterpret_cast<char*>(&current_byte), sizeof(current_byte));
                    current_byte=0;
                    bit_count=0;
                }
            }
        }
        if (bit_count > 0) {
            bit_file.write(reinterpret_cast<char*>(&current_byte), sizeof(current_byte));
        }
        bit_file.close();


    }
    else{
        cout<<"Cannot open one of the files";
    }


}