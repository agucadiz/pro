calcula = lambda s: suma if s == 'sum' else \
                    resta if s == 'res' else \
                    multiplica if s == 'mul' else \
                    divide if s == 'div' else 0

suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplica = lambda x, y: x * y
divide = lambda x, y: x / y

calcula('div')(calcula('mul')(2, 3), calcula('res')(9,3))
