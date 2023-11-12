import sample_module
import another_sample_module as asm
import sample_package.sample_module2
from new_sample_module import greeting as gsm
from random import *
# from sample_package import sample_module2
# import sample_package.sample_module2
import requests

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sample_module.greeting('Nav')
    asm.greeting('Nav')
    gsm('Nav')
    randint(1, 20)
    sample_package.sample_module2.do_something()
    requests.get('https://www.jetbrains.com/help/pycharm/')

