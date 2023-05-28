read -p "Enter the length of the rectangle: " length
read -p "Enter the breadth of the rectangle: " breadth
area=$(echo "scale=2; $length * $breadth" | bc)
echo "Area of the rectangle: $area square units"
