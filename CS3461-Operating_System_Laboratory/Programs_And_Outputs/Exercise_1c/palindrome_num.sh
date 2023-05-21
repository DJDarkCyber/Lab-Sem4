echo "Enter a number"
read a
d=$a
c=0
b=1
while [ $a -gt 0 ]
do
  b=`expr $a % 10`
  c=`expr $c \* 10 + $b`
  a=`expr $a / 10`
done
if [ $d -eq $c ]
then
  echo "PALINDROME"
else
  echo "NOT PALINDROME"
fi
