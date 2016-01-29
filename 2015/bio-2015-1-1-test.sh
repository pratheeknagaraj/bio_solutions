# Test file for Question 1

inputs=(
        'BBACBB'
        'XX'
        'YZ'
        'OLYMPIAD'
        'RACECAR'
        'KKKKKKK'
        'BBIIOIIBB'
        'PPPQQQQPPP'
        'AAAAAAAAAA'
        )

outputs=(
        "3\n"
        "1\n"
        "0\n"
        "0\n"
        "3\n"
        "7\n"
        "9\n"
        "19\n"
        "31\n"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2015-1-1.py > out.txt
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
