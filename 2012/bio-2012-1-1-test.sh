# Test file for Question 1

inputs=(
        '100'
        '101'
        '2'
        '1001'
        '371293'
        '789774'
        '999883'
        '561125'
        '661229'
        )

outputs=(
        "10\n"
        "101\n"
        "2\n"
        "1001\n"
        "13\n"
        "789774\n"
        "999883\n"
        "335\n"
        "4379\n"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2012-1-1.py > out.txt
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


