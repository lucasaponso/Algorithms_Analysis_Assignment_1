#!/bin/bash
GREEN_TICK="\e[32m\xE2\x9C\x94\e[0m"
reset="\033[0m"
red="\033[31m"


function array_unit()
{
    python3 dictionary_file_based.py array $1 $2 output.txt
    output=$(diff -s $3 output.txt)
     ((counter++))
    if [ "$output" == "Files $3 and output.txt are identical" ]; then
        echo -e "Unit Test Passed UID:$counter ${GREEN_TICK}"
    else
        
        echo -e "Unit Test Failed UID:$counter ${red}✗${reset}"
    fi
}


function linkedlist_unit()
{
    python3 dictionary_file_based.py linkedlist $1 $2 output.txt
    output=$(diff -s $3 output.txt)
     ((counter++))
    if [ "$output" == "Files $3 and output.txt are identical" ]; then
        echo -e "Unit Test Passed UID:$counter ${GREEN_TICK}"
    else
        
        echo -e "Unit Test Failed UID:$counter ${red}✗${reset}"
    fi
}


function trie_unit()
{
    python3 dictionary_file_based.py trie $1 $2 output.txt
    output=$(diff -s $3 output.txt)
     ((counter++))
    if [ "$output" == "Files $3 and output.txt are identical" ]; then
        echo -e "Unit Test Passed UID:$counter ${GREEN_TICK}"
    else
        
        echo -e "Unit Test Failed UID:$counter ${red}✗${reset}"
    fi
}


counter=0
echo -e "${red}ARRAY IMPLEMENTATION${reset}"
echo ""
echo -e "${red}sampleData.txt${reset}"
array_unit sampleData.txt test1.in test1.exp
array_unit sampleData.txt test2.in test2.exp
echo ""
echo -e "${red}sampleDataToy.txt${reset}"
array_unit sampleDataToy.txt testToy.in testToy.exp
echo ""



echo -e "${red}LINKEDLIST IMPLEMENTATION${reset}"
echo ""
echo -e "${red}sampleData.txt${reset}"
linkedlist_unit sampleData.txt test1.in test1.exp
linkedlist_unit sampleData.txt test2.in test2.exp
echo ""
echo -e "${red}sampleDataToy.txt${reset}"
linkedlist_unit sampleDataToy.txt testToy.in testToy.exp
echo ""



echo -e "${red}TRIE IMPLEMENTATION${reset}"
echo ""
echo -e "${red}sampleData.txt${reset}"
trie_unit sampleData.txt test1.in test1.exp
trie_unit sampleData.txt test2.in test2.exp
echo ""
echo -e "${red}sampleDataToy.txt${reset}"
trie_unit sampleDataToy.txt testToy.in testToy.exp
echo ""