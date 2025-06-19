# Learning the underlying physics of a simulation model of the ocean's temperature (CIRC23)

<p align="center">
    <a href="https://github.com/eds-book/3286b92f-4fae-4cc6-a29e-e408bc844542/actions/workflows/monthly-build.yaml/badge.svg">
        <img alt="Continuous integration badge" src="https://github.com/eds-book/3286b92f-4fae-4cc6-a29e-e408bc844542/actions/workflows/monthly-build.yaml/badge.svg">
    </a>
    <a href="http://mybinder.org/v2/gh/eds-book/3286b92f-4fae-4cc6-a29e-e408bc844542/main?labpath=notebook.ipynb">
        <img alt="Binder" src="https://mybinder.org/badge_logo.svg">
    </a>
    <a href="https://doi.org/10.5281/zenodo.8296922">
        <img alt="doi" src="https://zenodo.org/badge/636822482.svg">
    </a>
    <a href="https://github.com/eds-book/notebooks-reviews/issues/10">
        <img alt="notebook review" src="https://img.shields.io/badge/view-review-purple">
    </a>
</p>

<p align="center">
<img src="images/thumbnail.png" alt="thumbnail" width="500"/>
</p>

## How to run

### Running locally
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