# Test file for Question 2

inputs=(
        "2\n3 4\n6 5\n"
        "2\n2 4\n1 5\n"
        "3\n3 4 6\n6 5 6\n4 4 3\n"
        "3\n5 2 6\n1 6 1\n4 2 3\n"
        "4\n5 6 5 6\n4 3 4 3\n5 6 5 6\n4 3 4 3\n"
        "4\n5 6 3 4\n4 3 5 2\n5 6 4 2\n4 3 6 5\n"
        "5\n3 3 1 4 4\n3 5 2 6 4\n2 1 1 1 2\n6 4 2 3 5\n6 6 1 5 5\n"
        "6\n1 2 3 4 5 6\n5 6 6 5 4 3\n1 4 2 2 6 6\n4 2 6 3 1 4\n5 2 3 6 1 5\n4 2 2 2 3 3\n"
        )

outputs=(
        "0 4\n"
        "0 0\n"
        "4 4\n"
        "8 0\n"
        "16 4\n"
        "8 10\n"
        "8 16\n"
        "24 10\n")

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2014-1-2.py > out.txt
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
