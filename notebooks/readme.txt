## Reproducibility Challenge- Team 3

## This file provides instructions on creating the conda environment
## that has all the packages from ../environment.yml, which are 
## required to run ./notebook.ipynb

1. Create a new conda environment
   $ conda create -n newenv 

2. Activate the conda environment
   $ conda activate newenv

3. Install pykernels
   $ conda install -c anaconda ipykernel

4. To use this environment in jupyter notebook:
   $ ipython kernel install --user --name=newenv

5. Get the path to the new environment by running the following 
   command:
   $ conda info --envs

6. Use environment.yml to update the new environment
   $ conda env update --prefix path_to_env --file environment.yml 
   
   (If the above command doesn't work, try deactivating the environment
    and then running the above command)

7. Load the new environment in the jupyter notebook
