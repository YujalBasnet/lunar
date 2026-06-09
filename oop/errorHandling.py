try:
    a=10
    b="10"
    print(a+b)
except NameError as b:
    print("error",b)
    
except TypeError as b:
    print("typing error",b)
    
finally:
    print("yo chai j sukai huda ni run hunxa!!!!!!!")