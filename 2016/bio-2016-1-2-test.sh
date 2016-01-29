# Test file for Question 2
inputs=(
        "8 1 4\n0"
        "6 3 18\n3 5 11"
        "12 2 7\n1 24"
        "7 3 23\n2 9 14"
        "1 4 61\n4 16 4 1"
        "18 5 76\n2 2 24 23 4"
        "3 6 150\n2 3 5 7 11 13"
        "3 6 999\n2 3 5 7 11 13"
        )

outputs=(
        "00100\n01010\n00100\n00000\n00000\n"
        "11110\n11121\n00111\n10010\n11001\n"
        "00000\n01100\n11010\n01100\n00000\n"
        "02120\n21012\n02220\n01310\n00100\n"
        "01133\n12003\n10000\n30003\n33033\n"
        "13331\n31213\n32323\n31313\n13331\n"
        "23232\n32223\n22222\n32223\n23232\n"
        "23230\n22322\n32321\n31122\n03313\n"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2016-1-2.py > out.txt
    printf "$output" > check.txt


    diff out.txt check.txt >/dev/null
    if [ `echo $?`  -eq 0 ]
    then
        printf '\e[1;32mPass Test %s \e[0m\n' "$((test_num+1))"

    else
        printf '\e[0;31mFail Test %s \e[0m\n' "$((test_num+1))"
        printf "\e[0;31mGOT:\n"; cat out.txt
        printf "EXPECTED:\n"; cat check.txt
        printf "\e[0m\n"
    fi
    rm out.txt
    rm check.txt
done


#printf "GOT:\n"; printf "3 6 999\n2 3 5 7 11 13" | python bio-2016-1-2.py
#printf "EXPECTED: \n23230\n22322\n32321\n31122\n03313\n"
