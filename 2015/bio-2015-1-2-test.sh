# Test file for Question 2

printf "10 5 9999" | python bio-2015-1-2.py > out.txt
printf "6 0 V\n5 5 V\n0 6 H\n0 1 V\n7 2 V\n7 7 V\n2 8 H\n2 3 V\n9 4 V\n9 9 H\n" > check.txt

inputs=(
        "10 5 9999"
        "1 1 1000"
        "2 2 12345"
        "5 7 12346"
        "1 29209 32719"
        "16807 1 9999"
        )

outputs=(
        "5 0 V\n5 5 V\n0 6 H\n0 1 V\n7 2 V\n7 7 V\n2 8 H\n2 3 V\n9 4 V\n9 9 H\n"
        "1 0 H\n7 0 H\n1 2 H\n5 2 H\n1 4 H\n5 4 H\n9 4 H\n1 6 H\n3 6 H\n5 6 H\n"
        "2 0 H\n2 6 H\n2 2 H\n4 9 H\n7 3 H\n7 9 H\n9 5 H\n2 4 H\n7 5 V\n2 9 H\n"
        "1 1 H\n1 7 H\n1 5 H\n7 8 H\n3 3 H\n7 3 H\n5 6 H\n9 0 H\n1 9 H\n7 0 H\n"
        "9 0 V\n9 6 V\n7 6 V\n7 2 V\n5 0 V\n5 8 V\n5 6 V\n5 4 V\n3 6 V\n3 4 V\n"
        "1 0 V\n9 0 V\n3 6 V\n3 3 H\n8 7 H\n8 5 H\n6 6 H\n7 9 H\n5 8 V\n1 8 V\n"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2015-1-2.py > out.txt
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
