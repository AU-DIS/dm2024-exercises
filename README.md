# Exercises, Data Mining at Aarhus University
The [Data Mining course](https://kursuskatalog.au.dk/da/course/118146/Data-Mining) 
at Aarhus University is primarily based on the 

* [Data Mining and Analysis](https://dataminingbook.info/book_html/) book from Zaki and Meira referred to as [DMA] throughout this repository:

> Zaki, M.J., Meira Jr, W. and Meira, W., 2020. 
> Data mining and analysis: fundamental concepts 
> and algorithms. Cambridge University Press.

* [Mining of Massive Datasets](http://www.mmds.org/) book from Leskovec, Rajaraman, Ullman
refered to as [MMD] throughout this repository:

> Leskovec, J., Rajaraman, A. and Ullman, J.D., 2020. 
> Mining of massive data sets. Cambridge university press.

* [Graph Representation Learning](https://www.cs.mcgill.ca/~wlh/grl_book/) book from Hamilton referred to as [GRL] throughout this repository:

> Hamilton W. L., 2020. 
> Graph Representation Learning. 
> Synthesis Lectures on Artificial Intelligence and Machine Learning


**Note** that an online version of the book can be downloaded on the official
webpage, which is linked above. Furthermore, under the `Resources` tab on that
website, there are links to lecture videos, which might have value for you. 

> **Disclaimer:** the books lecture videos are _not_ part of the course material and
> are not guaranteed to cover the same aspects of the course material as the
> actual lectures. So use them with cause.

Additional material for the course can be found on Blackboard under the sections "Material".

## Structure of the repository
Every week, there will be a Jupyter Notebook with exercises. The notebooks can be found
in the [exercises directory](./exercises). 

## Practical considerations 
### Tools
_note_: This course is a Python course, so in case you are not familiar with
Python, you might want to familiarize your self with Python and
JupyterNotebooks. Also, one library, that we are going to be using a lot is
`numpy`, which allows us to work with vectors and matrices. Additional libraries will be introduced during the course

### Setup
If you don't have Python installed already, we recommend you to install 
[MiniConda](https://docs.conda.io/en/latest/miniconda.html). MiniConda allows
you to have different environments (think different python installations) for
each of your projects, such that you can keep dependencies separated.

Install MiniConda and then open a conda terminal. In there, you can then create
an environment, where we will install the necessary packages for this course.

_Navigate to the project directory_:
```bash
> cd /path/to/dm2024-exercises
```

_Create and activate environment:_  
```bash
> conda env create -f requirements.yml
> conda activate dm24
``` 

Now you should have created a conda environment with the necessary
dependencies.  From now on, when you want to run a python script or start a
notebook for this course, make sure to activate the environment (as in the last
line of coda above).  You know that your environment is active, if your active
line in the terminal is prefixed with `(dm24)`.

By the way, a pretty fine cheatsheet can be found 
[here](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf).

**Starting Jupyter Lab:**  
To edit Jupyter Notebooks, we need to start Jupyter lab. 
Navigate to the root of this repo and run the
following command from the command line:

```bash
(dm24) > jupyter lab
```

The command should open a new window in your browser, where you can start running
Python scripts.

Happy hacking. 

#### For Vim enthusiats
If you want vim-bindings in Jupyter Lab, then you can go to the extensions panel (on the left in
Jupyter Lab) and search for the library `jupyterlab_vim`.

