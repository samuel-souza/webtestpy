library(reticulate)
reticulate::py_run_file('script.py')


database = read.csv('bdd.csv')
jf = read.csv('jf.csv')
jf
database
