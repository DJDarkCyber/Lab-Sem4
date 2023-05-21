echo "Enter a Number"
read num
x=$num
sum=0
while [ $sum -gt 0 ]
do
  y=`expr $num % 10`
  z=`expr $y \* $y \* $y`
  sum=`expr $num / 10`
done
if [ $x -eq $sum ]
then
  echo "$x is an armstrong number"
else
  echo "$x is not an armstrong number"
fi
