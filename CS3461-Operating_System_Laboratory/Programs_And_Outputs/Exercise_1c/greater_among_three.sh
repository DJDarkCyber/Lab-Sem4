echo "Greatest of 3 numbers"
echo "Enter the numbers"
read a
read b
read c
if test $a -gt $b -a $a -gt $c
then
  echo "$a is greater"
elif test $b -gt $c
then
  echo "$b is greater"
else
  echo "$c is greater"
fi
