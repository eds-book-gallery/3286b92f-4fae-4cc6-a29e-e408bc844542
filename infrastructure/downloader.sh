# download source data to raw schema
mkdir -p ../data/raw/
cd ../data/raw/

zenodo_get 10.5281/zenodo.7919172

# unzip data
for f in *.gz
    do echo "Processing $f file..." 
    gzip -d "$f"
done

#Input output data
cd ../../outputs/
zenodo_get 10.5281/zenodo.7954232

# unzip data
for f in *.gz
    do echo "Processing $f file..." 
    tar -xzf "$f"
    rm "$f"
done

mv MODELS/* ../outputs/models/ && rm -rf MODELS
mv ITERATED_PREDICTION_ARRAYS/* ../outputs/predictions/ && rm -rf ITERATED_PREDICTION_ARRAYS

mkdir ../outputs/interim
mv trunc_io_arrays/* ../outputs/interim/ && rm trunc_io_arrays

rm md5sums.txt
