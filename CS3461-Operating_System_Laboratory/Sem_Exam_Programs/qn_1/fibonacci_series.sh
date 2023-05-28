echo "Enter the range to be displayed"
read n
a=0
b=1
s=0
echo "Fibonacci Series"
while test $s -le $n
do
  a=$b
  b=$s
  echo $s
  s=`expr $a + $b`
done
