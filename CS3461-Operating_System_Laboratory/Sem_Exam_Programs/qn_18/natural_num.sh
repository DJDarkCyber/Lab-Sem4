echo "Squares of First 10 Natural Numbers"
echo "-----------------------------------"

number=1

while [ $number -le 10 ]
do
    square=$((number * number))
    echo "Square of $number: $square"
    number=$((number + 1))
done
