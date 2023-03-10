>>> S = 'Spam'
#ejecutado
>>> S.find('pa')
# 1
>>> S
#'Spam'
>>> S.replace('pa', 'XYZ')
# 'SXYZm'
>>> S
#'Spam'
>>> line = 'aaa,bbb,ccccc,dd'
# Ejecutado
>>> line.split(',')
#['aaa', 'bbb', 'ccccc', 'dd']
>>> S = 'spam'
# Ejecutado
>>> S.upper()
#'SPAM'
>>> S.isalpha() # Content tests: isalpha, isdigit, etc.
# True
>>> line = 'aaa,bbb,ccccc,dd\n'
# Ejecutado
>>> line.rstrip()
#'aaa,bbb,ccccc,dd'
>>> line.rstrip().split(',')
#['aaa', 'bbb', 'ccccc', 'dd']
