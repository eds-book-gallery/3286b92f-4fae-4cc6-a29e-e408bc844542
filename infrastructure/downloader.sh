# download source data to raw schema
#mkdir ../data/
#mkdir ../data/raw/
#cd ../data/raw/

#zenodo_get 10.5281/zenodo.7919172

# unzip data
#for f in *.gz
#    do echo "Processing $f file..." 
#    gzip -d "$f"
#done

#Input output data
cd ../outputs/
zenodo_get 10.5281/zenodo.7954232

# unzip data
for f in *.gz
    do echo "Processing $f file..." 
    tar -xvf -d "$f"
done

mv MODELS ../outputs/models/
mv predictions ../outputs/predictions/
mkdir ../outputs/interim
mv trunc_io_arrays/* ../outputs/interim/
