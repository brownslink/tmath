""" MATH FILE PARSER """
from math import log, log10, pow, erfc, sqrt

def log2( p):
    return( log( p, 2))


def pow2( p):
    return( pow( 2, p))


def pow10( p):
    return( pow( 10, p))

steps = open( "problem-5c.math")

for step in steps:
    fields = step.split( ":")
    variable_fields = fields[ 0].split("=")
    variable = variable_fields[ 0].strip()
    expression = variable_fields[ 1].strip()
    description = fields[ 1].strip()
    units_fields = fields[ 2].strip().split( "//")
    units = units_fields[ 0]
    if( len( units_fields) < 2):
        units_factor = ""
    else:
        units_factor = "/"+units_fields[ 1]
    equation = ( variable + " = (" + expression + ")")
    exec( equation)
    variable_str = str( float( '%.4g' % eval( variable + units_factor)))
    line = ( variable + " = " + expression)
    if( not( variable_str == expression)):
        line += " = "+variable_str
    line += " "+units+" : "+description
    print( line)
