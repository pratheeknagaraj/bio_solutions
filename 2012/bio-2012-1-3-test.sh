# Test file for Question 3

inputs=(
        '26 61\n1 94\n1 610'
        '1 2\n1 3\n1 4'
        '14 543\n5 75\n71 713'
        '21 911\n329 927\n66 71'
        '250 361\n34 756\n18 735'
        '77 383\n48 677\n232 471'
        '220 691\n198 222\n410 666'
        '402 788\n203 959\n404 777'
        )

outputs=(
        "1\n1\n2\n"
        "1\n2\n1\n"
        "2\n1\n1\n"
        "2\n2\n3\n"
        "3\n4\n3\n"
        "5\n4\n4\n"
        "5\n5\n6\n"
        "6\n6\n6\n"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2012-1-3.py > out.txt
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

