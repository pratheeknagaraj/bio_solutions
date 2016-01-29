# Test file for Question 3

inputs=(
        'mnoqRTwxy'
        'N'
        'abcdef'
        'ABF'
        'gklmq'
        'ghkLNQSTwXy'
        'ghkLmNrTWXy'
        'abrs'
        'deHi'
        )

outputs=(
        "test1.txt"
        "test2.txt"
        "test3.txt"
        "test4.txt"
        "test5.txt"
        "test6.txt"
        "test7.txt"
        "test8.txt"
        "test9.txt"
        )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2013-1-3.py > out.txt
    check="q3_out/$output"

    out=`cat out.txt`

    grep -Fq "$out" $check >/dev/null
    if [ `echo $?`  -eq 0 ]
    then
        printf '\e[1;32mPass Test %s \e[0m\n' "$((test_num+1))"

    else
        printf '\e[0;31mFail Test %s \e[0m\n' "$((test_num+1))"
        printf "\e[0;31mGOT:\n"; cat out.txt
        printf "EXPECTED: (check $output file)\n";
        printf "\e[0m\n"
    fi
    rm out.txt
done

