mkdir data
mkdir img
cd data
mkdir articles
mkdir new
touch alldata.csv
touch wranglerdata.json
echo {\"data\": []} >> wranglerdata.json
echo time,length,rubrik,author,keywords, \n >> alldata.csv
cd articles
touch articles.json
echo {\"data\": []} >> articles.json
cd ..
cd new
touch site.json
echo {\"data\": []} >> site.json