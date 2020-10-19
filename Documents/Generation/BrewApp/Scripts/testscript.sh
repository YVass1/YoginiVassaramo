
set -eu

echo -n "Enter a number: "
read var

if [[ $var -gt 10 ]]
then
    echo "greater than 10"
else
    echo "less then 10"
fi
