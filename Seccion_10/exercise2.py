def infinite_UpperCase(*args):
    return sorted([arg.upper() for arg in args])
    

print(infinite_UpperCase("snow", "glacier", "iceberg"))