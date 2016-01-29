# Test file for Question 3

inputs=(
        '1'
        '21'
        '321'
        '4321'
        '54321'
        '654321'
        '7654321'
        '87654321'
        '234234234'
        '987654321'
        )

outputs=(
        "A\n"
        "U\n"
        "JP\n"
        "HPQ\n"
        "LNOV\n"
        "AHJSVW\n"
        "EHJK025\n"
        "CEILRU059\n"
        "BEHJPVX267\n"
        "MNOPQTUX026\n"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2014-1-3.py > out.txt
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

