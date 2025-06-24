class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x  # Начальная координата X
        self.y = y  # Начальная координата Y
        self.s = s  # Размер шага (количество клеток за ход)
    
    def go_up(self):
        """Перемещает черепашку вверх по оси Y"""
        self.y += self.s
    
    def go_down(self):
        """Перемещает черепашку вниз по оси Y"""
        self.y -= self.s
    
    def go_left(self):
        """Перемещает черепашку влево по оси X"""
        self.x -= self.s
    
    def go_right(self):
        """Перемещает черепашку вправо по оси X"""
        self.x += self.s
    
    def evolve(self):
        """Увеличивает размер шага на 1"""
        self.s += 1
    
    def degrade(self):
        """
        Уменьшает размер шага на 1.
        Вызывает исключение, если шаг становится ≤ 0.
        """
        if self.s <= 1:
            raise ValueError("Шаг не может быть меньше или равен 0")
        self.s -= 1
    
    def count_moves(self, x2, y2):
        """
        Рассчитывает минимальное количество действий для достижения цели.
        Каждое движение (вверх/вниз/влево/вправо) считается отдельным действием.
        """
        dx = abs(x2 - self.x)  # Расстояние по X
        dy = abs(y2 - self.y)  # Расстояние по Y
        
        # Рассчитываем количество шагов для каждой оси
        steps_x = (dx + self.s - 1) // self.s if dx > 0 else 0
        steps_y = (dy + self.s - 1) // self.s if dy > 0 else 0
        
        return steps_x + steps_y