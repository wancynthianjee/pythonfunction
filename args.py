def my_country(country='Rwanda'):
    print(f"Hello {country}")

def sum(*numbers):
    answer=0
    for number in numbers:
        answer+=number
    return output

def multiply(*nums):
    output=1
    for num in nums:
        output *= num
    return output

def concatenate_arg(*args):
    str=""
    for arg in args:
        output=arg
    print(output) 

# def concatenate_args(*names):
#     for name in names:
#         print(f"Hello +{name}")
def concatenate_kwargs(**kwargs):
    answer = ""
    for key,value in kwargs.items():
        answer+=value
    return answer