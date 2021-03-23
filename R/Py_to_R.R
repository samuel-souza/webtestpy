#' Function Py_to_R
#' This function used a script made in Python language
#' and needs two arguments to peform correctly, returning two data frames.
#' @directory : argument that set a directory of script py.
#' @script_name : argument for run a script py.



Py_to_R = function (directory) {

    if (typeof(directory) != 'character') {
    print('you need use as an argument a directory of script .py')
  }
    if ('reticulate' %in% rownames(installed.packages())) {
    library('reticulate')
    reticulate::py_run_file(as.character(directory))
  }
    else {
    install.packages('reticulate')
    library(reticulate)
    reticulate::py_run_file(as.character(directory))
  }
    database <<- read.csv('bdd.csv',encoding = 'latin1')
    if (file.exists('jf.csv')){

    future_matches <<- read.csv('jf.csv',encoding = 'latin1')
    file.remove(c('bdd.csv','jf.csv'))
    return(database)
    return(future_matches)
  }
  else {
    file.remove('bdd.csv')
  }


  return(database)

}


