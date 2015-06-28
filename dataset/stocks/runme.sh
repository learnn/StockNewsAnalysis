mkdir dataset
npm install underscore csvtojson

/usr/bin/node s1.js
echo "---------------------------------END OF STEP 1----------------------------------"
mv *.csv dataset/
mv dataset/test.csv .
./s2.sh
echo "Done"
