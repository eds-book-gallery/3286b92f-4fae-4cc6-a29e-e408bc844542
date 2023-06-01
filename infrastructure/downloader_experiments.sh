# download input to run notebook
cd ../outputs/

zenodo_get 10.5281/zenodo.7954232

# unzip data
for f in *.gz
    do echo "Processing $f file..." 
    tar -xzf "$f"
    rm "$f"
done

mv MODELS/* models/ && rm -rf MODELS
mv ITERATED_PREDICTION_ARRAYS/* predictions/ && rm -rf ITERATED_PREDICTION_ARRAYS
mv trunc_io_arrays/* ../data/interim/ && rm -rf trunc_io_arrays
rm md5sums.txt
