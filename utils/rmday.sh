#! /bin/bash

cd /Users/will/Documents/Projects/adventofcode/

DAYNUM=${@: -1}
printf -v padded "%02d" $DAYNUM  # pad the number provided


function rmif() {
    if [ -f $1 ]; then
        rm $1
        echo " - Succesfully removed: $1"
    else
        echo " - File not found: $1"
    fi
}

# Parse options
NODATA=false
HELP=false

while getopts "o:n:h:" opt; do
    case $opt in
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
    echo " -- REMOVE DAY - HELP -- "
    echo ""
    echo "OPTIONS:"
    echo "  n: [optional, defaults to false, only specify when true]"
    echo "       NODATA option. Will not look for/remove the data file."
    echo "  h: [optional, defaults to false, only specify when true]"
    echo "       Runs HELP message"
    echo ""
    echo "USAGE:"
    echo ">>./utils/rmday.sh [-n] <day-number>"
    echo ""
    exit 0
fi


# Remove files
echo ""
if ! $NODATA; then
    rmif data/d${padded}.txt
fi

rmif day${padded}.py
echo ""


exit 0
