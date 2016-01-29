# Test file for Question 3

# Test file for Question 3

inputs=(
        "100 2 13"
        "20 2 3"
        "20 2 13"
        "100 73 89"
        "100 19 97"
        "1000 3 971"
        "2000 977 997"
        "5000 83 3643"
        "614700 3643 90149"
        "987654 3643 90149"
        "1000000 2 968137"
        "1000000 993851 995387"
        )

outputs=(
        "4\n"
        "2\n"
        "4\n"
        "2\n"
        "7\n"
        "9\n"
        "4\n"
        "10\n"
        "18\n"
        "16\n"
        "18\n"
        "3\n"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2016-1-3.py > out.txt
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

