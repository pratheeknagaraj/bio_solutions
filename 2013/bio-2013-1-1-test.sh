# Test file for Question 1

inputs=(
        '1 31'
        '0 0'
        '18 18'
        '67 1507'
        '0 15'
        '0 7'
        '17 26'
        '17 215'
        '5779 5864'
        '21923 26268'
        )

outputs=(
        "00:48\n"
        "01:00\n"
        "01:18\n"
        "02:07\n"
        "00:00\n"
        "00:00\n"
        "13:20\n"
        "06:40\n"
        "19:12\n"
        "14:24\n"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2013-1-1.py > out.txt
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


