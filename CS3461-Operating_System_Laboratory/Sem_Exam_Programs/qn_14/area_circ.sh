echo -n "Enter the radius of the cicle > "
read r

area=$(echo "scale=2; 3.14 * $r * $r" | bc)
circumference=$(echo "scale=2; 2 * 3.14 * $r" | bc)

echo "Area : $area"
echo "Circumference : $circumference"
