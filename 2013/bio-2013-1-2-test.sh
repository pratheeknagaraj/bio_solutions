# Test file for Question 2

inputs=(
        "1 2 3 4 5\n1 2 3 4 5"
        "5 2 4 1 3\n1 4 2 3 5"
        "1 4 3 5 2\n2 3 4 1 5"
        "1 3 5 4 2\n4 1 2 5 3"
        "3 4 1 5 2\n3 4 1 5 2"
        )

outputs=(
        "SSSSS\nF.*..\n.....\n.....\n.FFFF\n\n.SSSS\nF...*\n.....\n...S.\n.FFFF\n\n..SSS\nFF...\n.....\n...SS\n.*FFF\n"
        "SSSSS\n..*.F\n.....\n.....\nFFFF.\n\n.SSSS\n...*F\n.....\n.....\nFFFFS\n\n.FF.F\n...SS\n....S\n...F.\nSS*.F\n"
        "SSSSS\nF.*..\n.....\n.....\n.FFFF\n\nS.SSS\nF...*\n.....\n....S\n.FFFF\n\nFFSSF\n.....\n....S\nS..F.\n*.F.S\n"
        "SSSSS\nF.*..\n.....\n.....\n.FFFF\n\nSSS.S\nF...*\n.....\n...S.\n.FFFF\n\n..S..\nF.FSF\n..SF*\n.S.SF\n.....\n"
        "SSSSS\n..*..\n..F..\n.....\nFF.FF\n\nSS.SS\n....*\n..F.S\n.....\nFF.FF\n\n..S.*\n.S.F.\n..FSS\nSF..F\n....F\n"
    )

length=${#inputs[@]}

for (( test_num=0; test_num<${length}; test_num++ ));
do
    input=${inputs[$test_num]}
    output=${outputs[$test_num]}

    printf "$input" | python bio-2013-1-2.py > out.txt
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
