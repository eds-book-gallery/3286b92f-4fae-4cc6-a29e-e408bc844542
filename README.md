<div align="center">
    <h6>Environmental Data Science Book</h6>
</div>

<p align="center">
<img src="https://github.com/alan-turing-institute/environmental-ds-book/blob/master/book/figures/logo/logo.png?raw=True" alt="thumbnail" width="200"/>
</p>

<div align="center">
    <h1>Learning the underlying physics of a simulation model of the ocean's temperature (CIRC23)</h1>
</div>

<p align="center">
    <a href="https://github.com/eds-book-gallery/3286b92f-4fae-4cc6-a29e-e408bc844542/blob/main/LICENSE">
        <img alt="license" src="https://img.shields.io/badge/license-MIT-yellow.svg">
    </a>
    <a href="https://notebooks.gesis.org/binder/v2/gh/eds-book-gallery/3286b92f-4fae-4cc6-a29e-e408bc844542/main?labpath=notebook.ipynb">
        <img alt="binder" src="https://mybinder.org/badge_logo.svg">
    </a>
    <a href="https://github.com/eds-book-gallery/3286b92f-4fae-4cc6-a29e-e408bc844542/actions/workflows/render.yaml">
        <img alt="render" src="https://github.com/eds-book-gallery/3286b92f-4fae-4cc6-a29e-e408bc844542/actions/workflows/render.yaml/badge.svg">
    </a>
    <a href="https://github.com/alan-turing-institute/environmental-ds-book/issues/172">
        <img alt="review" src="https://img.shields.io/badge/view-revixew-purple">
    </a>
    <br/>
</p>

<p align="center">
    <a href="https://w3id.org/ro-id/62628420-93f5-4ed6-8178-f09bddabfca3">
        <img alt="RoHub" src="https://img.shields.io/badge/RoHub-FAIR_Executable_Research_Object-2ea44f?logo=Open+Access&logoColor=blue">
    </a>
    <a href="https://zenodo.org/badge/latestdoi/636822482">
        <img alt="doi" src="https://zenodo.org/badge/636822482.svg">
    </a>
</p>

<p align="center">
<img src="https://www.commondreams.org/media-library/ocean-surface-temperatures.jpg?id=33699188&width=1200&height=400&quality=90&coordinates=0%2C667%2C0%2C667" alt="thumbnail" width="500"/>
</p>

# How to run

## Running locally
You may also download the notebook from GitHub to run it locally:
1. Open your terminal

2. Check your conda install with `conda --version`. If you don't have conda, install it by following these instructions (see [here](https://docs.conda.io/en/latest/miniconda.html))

3. Clone the repository
    ```bash
    git clone https://github.com/eds-book-gallery/3286b92f-4fae-4cc6-a29e-e408bc844542.git
    ```

4. Move into the cloned repository
    ```bash
    cd 3286b92f-4fae-4cc6-a29e-e408bc844542
    ```

5. Create and activate your environment from the `.binder/environment.yml` file
    ```bash
    conda env create -f .binder/environment.yml
    conda activate 3286b92f-4fae-4cc6-a29e-e408bc844542
    ```  

6. Launch the jupyter interface of your preference, notebook, `jupyter notebook` or lab `jupyter lab`

# Credits
The **How to run** section was adapted from the [Project Pythia Cookbook](https://cookbooks.projectpythia.org/) project.