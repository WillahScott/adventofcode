#! /bin/bash

cd /Users/will/Documents/Projects/adventofcode/

DAYNUM=${@: -1}
printf -v padded "%02d" $DAYNUM  # pad the number provided


# Parse options
OPENSUB=true
NODATA=false
HELP=false

while getopts "o:n:h:" opt; do
    case $opt in
        o)
            OPENSUB=$OPTARG;;
        n)
            NODATA=true;;
        h)
            HELP=true;;
        \?)
            echo "Invalid option: -$OPTARG"
            exit 1;;
        :)
            echo "Option -$OPTARG requires an argument"
            exit 1;;
    esac
done


# Help message
if $HELP; then
    echo " -- NEW DAY - HELP -- "
    echo ""
    echo "OPTIONS:"
    echo "  o: [optional, defaults to true, only specify when -o false]"
    echo "       OPEN-SUBLIME option. Will not open a new sublime window."
    echo "  n: [optional, defaults to false, only specify when true]"
    echo "       NODATA option. Will not prepare a data file."
    echo "  h: [optional, defaults to false, only specify when true]"
    echo "       Runs HELP message"
    echo ""
    echo "USAGE:"
    echo ">>./utils/newday.sh [-n true -o false] <day-number>"
    echo ""
    exit 0
fi

if $OPENSUB; then
    # Open Sublime with the AoC project
    subl /Users/will/Documents/Projects/adventofcode/
fi


## Prepare data

if ! $NODATA; then
    # Create and open the data file
    echo ""
    echo " - Preparing data file: data/d${padded}.txt"
    echo ""
    touch data/d${padded}.txt
    subl data/d${padded}.txt
else
    echo ""
    echo " - No data file prepared"
    echo ""
fi


## Prepare code

t_start="# Advent of code - DAY ${DAYNUM}"$'\n\n'  # single quotes for \n

if ! $NODATA; then
    t_data="# Read data
with open('data/d${padded}.txt') as f:
    orig_data = [int(x) for x in f.readlines()]
"
else
    t_data=""
fi

t_body="

# -- Problem 1 function --
def part1(data, verbose=False):
    pass

# Test
part1(test, verbose=True)
  # > ?

# Run problem 1
part1(data)
  # > ?



# -- Problem 2 function --
def part2(data, verbose=False):
    pass

# Test
part2(test, verbose=True)
  # > ?

# Run problem 1
part2(data)
  # > ?
"

echo "$t_start$t_data$t_body" > day${padded}.py

echo " - Preparing code: day${padded}.py"
echo ""
subl day${padded}.py


exit 0
