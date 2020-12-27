class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)

    def decorator_instance(func):
        def wrapper(*args, **kwargs):
            if isinstance(args[1], int):
                func(*args, **kwargs)
            else:
                print('Введено не целочисленное значение!')

        return wrapper

    @decorator_instance
    def set_x(self, value):
        self.x = value

    def get_x(self):
        return self.x

    @decorator_instance
    def set_y(self, value):
        self.y = value

    def get_y(self):
        return self.y

    @decorator_instance
    def set_width(self, value):
        self.width = value

    def get_width(self):
        return self.width

    @decorator_instance
    def set_height(self, value):
        self.height = value

    def get_height(self):
        return self.height

    def get_print_data(self):
        return f'Rectangle ({self.x}, {self.y}, {self.width}, {self.height})'