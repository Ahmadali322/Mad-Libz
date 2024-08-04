#include <iostream>
#include <string>

using namespace std;

void big_story() {
    string animal, name, name2, adjective1, noun1, noun2, food, adjective2, name3, noun3, adjective3;
    string adjective4, noun4, adjective5, noun5;

    // Prompt for input
    cout << "Enter an Animal: ";
    getline(cin, animal);
    cout << "Enter a Name: ";
    getline(cin, name);
    cout << "Enter another Name: ";
    getline(cin, name2);
    cout << "Enter an Adjective: ";
    getline(cin, adjective1);
    cout << "Enter a Noun: ";
    getline(cin, noun1);
    cout << "Enter another Noun: ";
    getline(cin, noun2);
    cout << "Enter a Food: ";
    getline(cin, food);
    cout << "Enter another Adjective: ";
    getline(cin, adjective2);
    cout << "Enter a Fairy Name: ";
    getline(cin, name3);
    cout << "Enter a Noun: ";
    getline(cin, noun3);
    cout << "Enter another Adjective: ";
    getline(cin, adjective3);
    cout << "Enter another Adjective: ";
    getline(cin, adjective4);
    cout << "Enter another Noun: ";
    getline(cin, noun4);
    cout << "Enter another Adjective: ";
    getline(cin, adjective5);
    cout << "Enter another Noun: ";
    getline(cin, noun5);

    // Output the story
    cout << "In a faraway kingdom, there was an enchanted forest where magical creatures lived. The forest was guarded by a wise old " << animal << " named " << name << ". One day, a young adventurer named " << name2 << " decided to explore the forest. Armed with a " << adjective1 << " " << noun1 << " and a map given by a mysterious " << noun2 << ", " << name2 << " ventured into the forest. The trees were " << adjective2 << ", and the air was filled with the scent of " << food << ". As " << name2 << " walked deeper, they encountered a " << adjective3 << " fairy named " << name3 << " who needed help finding a lost " << noun3 << ". Together, they navigated through the " << adjective4 << " forest, facing challenges like crossing a " << adjective5 << " river and solving a riddle from a " << adjective3 << " troll. \n\nAfter hours of searching, they found the lost " << noun3 << " in a cave guarded by a " << adjective5 << " dragon. Using their " << noun1 << ", " << name2 << " managed to distract the dragon while " << name3 << " retrieved the " << noun3 << ". Grateful, the fairy rewarded " << name2 << " with a " << adjective3 << " gem that granted one wish. " << name2 << " wished for the forest to always be protected. The wish came true, and the enchanted forest remained safe forever. " << name2 << " returned to their village as a hero, and the story of their adventure was told for generations." << endl;
}

void mid_story() {
    string place, name, adjective1, noun1, adjective2, animal, noun2, adjective3, plural_noun, adjective4, noun3;

    // Prompt for input
    cout << "Enter a Place: ";
    getline(cin, place);
    cout << "Enter a Name: ";
    getline(cin, name);
    cout << "Enter an Adjective: ";
    getline(cin, adjective1);
    cout << "Enter a Noun: ";
    getline(cin, noun1);
    cout << "Enter another Adjective: ";
    getline(cin, adjective2);
    cout << "Enter an Animal: ";
    getline(cin, animal);
    cout << "Enter another Noun: ";
    getline(cin, noun2);
    cout << "Enter another Adjective: ";
    getline(cin, adjective3);
    cout << "Enter a Plural Noun: ";
    getline(cin, plural_noun);
    cout << "Enter another Adjective: ";
    getline(cin, adjective4);
    cout << "Enter another Noun: ";
    getline(cin, noun3);

    // Output the story
    cout << "Once upon a time, in the land of " << place << ", there lived a brave explorer named " << name << ". " << name << " loved to discover new places and find hidden treasures. One day, they found a mysterious map that led to a " << adjective1 << " treasure. With their trusty " << noun1 << " in hand, they set off on their journey. Along the way, they encountered a " << adjective2 << " " << animal << " that tried to steal their map. Using their " << noun1 << ", " << name << " managed to scare off the " << animal << ". After days of traveling through " << adjective3 << " forests and crossing " << adjective2 << " rivers, " << name << " finally found the treasure chest. Inside, there were " << plural_noun << " and a " << adjective4 << " " << noun3 << ". " << name << " returned home as a hero, and the people of " << place << " celebrated their " << adjective4 << " adventure." << endl;
}

void small_story() {
    string name, noun, food, adj, animal, verb;

    // Prompt for input
    cout << "Enter a Name: ";
    getline(cin, name);
    cout << "Enter a Noun: ";
    getline(cin, noun);
    cout << "Enter a Food: ";
    getline(cin, food);
    cout << "Enter an Adjective: ";
    getline(cin, adj);
    cout << "Enter an Animal: ";
    getline(cin, animal);
    cout << "Enter a Verb: ";
    getline(cin, verb);

    // Output the story
    cout << "One sunny day, " << name << " decided to visit the park. They brought their favorite " << noun << " and a delicious " << food << ". As they walked, they saw a " << adj << " " << animal << " playing with a " << noun << ". Suddenly, it started to " << verb << ", making everyone laugh. It was a " << adj << " day that " << name << " would never forget." << endl;
}

int main() {
    int ch;
    cout << "Choose your story length:\n1) Small\n2) Medium\n3) Large\n>> ";
    cin >> ch;
    cin.ignore();  // To ignore the newline character left in the buffer

    switch (ch) {
        case 1:
            small_story();
            break;
        case 2:
            mid_story();
            break;
        case 3:
            big_story();
            break;
        default:
            cout << "Invalid choice. Please choose 1, 2, or 3." << endl;
            break;
    }

    return 0;
}

