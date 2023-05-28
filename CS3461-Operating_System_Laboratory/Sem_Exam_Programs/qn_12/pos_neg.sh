echo -n "Enter a Number > "
read n

if [ $n -lt 0 ]; then
  echo "It is a negative number."
elif [ $n -gt 0 ]; then
  echo "It is a positive number."
else
  echo "It is zero."
fi
