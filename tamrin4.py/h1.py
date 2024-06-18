def cel_to_faranhaite (c) :
    return (c* 9/5) + 32


celsius_to_faran = [5, 10, 65, 95]
fahrenheit = list(map(cel_to_faranhaite,celsius_to_faran))
print (fahrenheit)