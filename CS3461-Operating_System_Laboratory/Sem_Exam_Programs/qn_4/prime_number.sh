echo "Enter a Number"
read n
i=`expr $n - 1`
t=0
while [ $i -ge 2 ]
do
  p=`expr $n % $i`
  if [ $p -eq 0 ]
  then
    t=`expr $t + 1`
  fi
  i=`expr $i - 1`
done
if [ $t -gt 0 ]
then
  echo "The number $n is not a prime number"
else
  echo "The number $n is a prime number"
fi
