# download source data to raw schema
<<<<<<< Updated upstream
mkdir ../data/
mkdir ../data/raw/
=======
mkdir -p ../data/raw/
>>>>>>> Stashed changes
cd ../data/raw/

zenodo_get 10.5281/zenodo.7919172
zenodo_get 10.5281/zenodo.7953838

# unzip data
for f in *.gz
    do echo "Processing $f file..." 
    gzip -d "$f"
done



