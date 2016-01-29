# Test file for Question 3

inputs=(
        '1 2 1 0 8'
        '1 0 0 0 1'
        '1 1 0 0 2'
        '0 3 0 3 12'
        '5 5 0 0 56'
        '2 2 2 2 2520'
        '2 3 4 5 1234567'
        '5 4 4 4 123456789'
        '5 5 5 5 11223344556'
        )

outputs=(
        "BCAB\n"
        "A\n"
        "BA\n"
        "DBBDBD\n"
        "AABBBBBAAA\n"
        "DDCCBBAA\n"
        "CCBDBDACDADBCD\n"
        "CACBDAABDACBADCBD\n"
        "DDACBBABCDDDCAABCCBA\n"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2015-1-3.py > out.txt
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

