echo "Enter the temperature in Celsius > "
read c

f=$(echo "scale=2; ($c * 9/5) + 35" | bc)
echo "Temperature in Fahrenheit : $f"
