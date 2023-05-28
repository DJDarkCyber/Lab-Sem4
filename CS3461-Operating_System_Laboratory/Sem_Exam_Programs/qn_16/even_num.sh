count=0
number=0

while [ $count -lt 10 ]
do
    if [ $((number % 2)) -eq 0 ]
    then
        echo $number
        count=$((count + 1))
    fi
    number=$((number + 1))
done
