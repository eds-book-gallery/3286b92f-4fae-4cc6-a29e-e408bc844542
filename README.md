<div align="center">
    <h6>Environmental Data Science Book</h6>
</div>

<p align="center">
<img src="https://github.com/alan-turing-institute/environmental-ds-book/blob/master/book/figures/logo/logo.png?raw=True" alt="thumbnail" width="200"/>
</p>

<div align="center">
    <h1>Learning the Underlying Physics of a Simulation Model of the Ocean's Temperature</h1>
</div>

# How to run

## Running locally
You may also download the notebook from GitHub to run it locally:
1. Open your terminal

2. Check your conda install with `conda --version`. If you don't have conda, install it by following these instructions (see [here](https://docs.conda.io/en/latest/miniconda.html))

3. Clone the repository
    ```bash
    git clone https://github.com/eds-book-gallery/repro-challenge-team-3.git
    ```

4. Move into the cloned repository
    ```bash
    cd repro-challenge-team-3
    ```

5. Change to the `review` branch. This will ensure you are launching the latest version of the notebook.
    ```bash
    git checkout review
    ```  
   
6. Create and activate your environment from the `environment.yml` file
    ```bash
    conda env create -f environment.yml
    conda activate team3-main-notebook
    ```  

7. Launch the jupyter interface of your preference, notebook, `jupyter notebook` or lab `jupyter lab`

# Credits
The **How to run** section was adapted from the [Project Pythia Cookbook](https://cookbooks.projectpythia.org/) project.