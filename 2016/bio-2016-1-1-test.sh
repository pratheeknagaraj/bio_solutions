# Test file for Question 1

inputs=(
        'L'
        'R'
        'LRLL'
        'LLRLR'
        'LLLRRR'
        'LLRRLL'
        'RRRLRRR'
        'LLLLRLLLL'
        'LLLLLLLLLL'
        'LRLRLRLRLR'
        )

outputs=(
        "1 / 2\n"
        "2 / 1\n"
        "4 / 7\n"
        "5 / 13\n"
        "4 / 13\n"
        "7 / 17\n"
        "19 / 5\n"
        "6 / 29\n"
        "1 / 11\n"
        "89 / 144\n"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2016-1-1.py > out.txt
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

