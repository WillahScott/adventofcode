#! /bin/bash

cd /Users/will/Documents/Projects/adventofcode/

DAYNUM=${@: -1}
printf -v padded "%02d" $DAYNUM  # pad the number provided


# Parse options
NODATA=false
HELP=false

while getopts "n:h:" opt; do
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
    echo " -- GIT COMMIT DAY - HELP -- "
    echo ""
    echo "OPTIONS:"
    echo "  n: [optional, defaults to false, only specify when true]"
    echo "       NODATA option. Will not look for/remove the data file."
    echo "  h: [optional, defaults to false, only specify when true]"
    echo "       Runs HELP message"
    echo ""
    echo "USAGE:"
    echo ">>./utils/gitday.sh [-n] <day-number>"
    echo ""
    exit 0
fi


# Remove files
echo ""
if ! $NODATA; then
    git add data/d${padded}.txt
fi

git add day${padded}.py

git commit -m "Day ${padded} - done"
echo " - Committed!"
echo ""

# Push
echo " - Pushing..."
git push
echo ""

# Log history
echo " - HISTORY: "
git log --oneline
echo ""


exit 0
