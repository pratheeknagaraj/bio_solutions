# Test file for Question 1

inputs=(
        '5'
        '33'
        '34'
        '399'
        '456'
        '3301'
        '3304'
        '9703'
        '10000'
        )

outputs=(
        "3 7\n"
        "31 37\n"
        "33 37\n"
        "393 409\n"
        "451 463\n"
        "3297 3307\n"
        "3301 3307\n"
        "9691 9727\n"
        "9999 10003\n"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2014-1-1.py > out.txt
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


