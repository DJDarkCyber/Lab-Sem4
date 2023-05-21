echo "Enter the limit"
read n
echo "Enter the $n numbers"
sum=0
i=1
while test $i -le $n
do
  read num
  sum=`expr $num + $sum`
  i=`expr $i + 1`
done
echo "The of the numbers are $sum"
