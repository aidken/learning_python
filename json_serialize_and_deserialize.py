import sys, io
import logging
import pprint
from dataclasses import dataclass, field
import json
pp = pprint.PrettyPrinter(indent=4)


# cSpell:ignore sqlite serializable datefmt

@dataclass
class MyClass:
    a: str
    b: int

    def __post_init__(self):
        self.a = str(self.a)
        self.b = int(self.b)

    def encode_to_json(self) -> dict:
        if isinstance(self, MyClass):
            return{
                f'__{self.__class__.__name__}__': 1,
                'a': self.a,
                'b': self.b
            }
        else:
            raise TypeError(f'Object type "{type(self)}" is not a MyClass, not JSON serializable.')

    def decode_from_json(json_str: str) -> json:
        tmp = json.loads(json_str)
        return MyClass(
            a = tmp['a'],
            b = tmp['b']
        )


def main():
    x = MyClass(a='abc', b=123)
    print(x)
    print('x is a ' + x.__class__.__name__)

    print('Encoding this x to JSON and put it into var y.')
    y = json.dumps(x, indent=4, default=MyClass.encode_to_json)
    print('JSON serialized x is ' + y)
    print(f'y is a {y.__class__.__name__}.')
    print('Let\'s decode y.')
    z = MyClass.decode_from_json(y)
    print(z)
    print('z is a ' + x.__class__.__name__)



if __name__ == '__main__':

    # https://qiita.com/jack-low/items/91bf9b5342965352cbeb
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # logger setup
    filename = str(sys.argv[0])[:-3] + '.log'
    format = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)-8s: %(message)s'
    logging.basicConfig(
        filename = filename,
        format   = format,
        datefmt  = '%m-%d %H:%M',
        level    = logging.INFO,
        # level    = logging.DEBUG,
        # level    = logging.ERROR,
    )

    # https://docs.python.org/3/howto/logging-cookbook.html#logging-to-multiple-destinations
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    main()
