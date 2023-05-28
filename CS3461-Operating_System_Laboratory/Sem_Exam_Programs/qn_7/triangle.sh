echo "Enter the base of the triangle > "
read b
echo "Enter the height of the triangle > "
read h

area=$(echo "scale=2; 0.5 * $b * $h" | bc)

echo "Area of the triangle: $area square units"
