from django.db import models

# т.к. эти данные будут вносится в базы данных
# А базы данных имеют строгую типизацию
# Нужно сделать строгую типизацию переменных

class Categories(models.Model):

    name=models.CharField(
        max_length=150, 
        blank=True, 
        null=True, 
        # unique=True, 
        # verbose_name='Название Категории'
        )
    
    name_two=models.CharField(
        max_length=150, 
        # default="null"
        # unique=True, 
        blank=True, 
        null=True, 
        # verbose_name='Название Подкатегории'
        )
    
    # slug=models.SlugField(
    #     max_length=350, 
    #     # unique=True, 
    #     blank=True, 
    #     null=True, 
    #     verbose_name='URL'
    #     )

    # Данный вложенный класс создает в базе данных sql папку с именем 'category'
    # Для родительского класса Categories

    class Meta:
        # db-table - по умолчанию в базе данных имя столбца присвается как "ИмяПриложения_Модель"
        # С помощью данного поля можно его изменить на любое.
        db_table='category'
        verbose_name='Категория'
        verbose_name_plural='Категории'

    def __str__(self):
        return str(self.name)

class Products(models.Model):
    # CharField - Поле, с помощью которого можно создать переменную типа 'char' в БД
    # Применятся для хранения не большой строки
    name=models.CharField(
        # max_length-максимальная длина хранения строки
        max_length=150, 
        # unique - каждой сроке будет присвоен уникальный индентификатор
        unique=True, 
        # verbose_name - поле, которое переименовывает переменную name в БД
        verbose_name='Название'
        )
    
    slug=models.SlugField(
        max_length=350, 
        unique=True, 
        # blank - Разрешает поле быть пустым на уровне форм Django.
        blank=True, 
        # null - Разрешает полю slug быть пустым (в базе данных будет сохранено как NULL). 
        null=True, 
        verbose_name='URL'
        )
    
    # TextField - Поле, в котором можно хранить большой текст в БД
    description=models.TextField(
        blank=True, 
        null=True, 
        verbose_name='Описание'
        )
    
    # TextField - Поле, с помощью которого в БД можно передавать картинки.
    image=models.ImageField(
        upload_to='goods_images',
        blank=True, 
        null=True,
        verbose_name='Изображение'
        )
    # DecimalFiel - Поле, которое позволяет опреелять не целые числа.
    price=models.DecimalField(
        default=0.00, 
        max_digits=7, 
        decimal_places=2,
        verbose_name='Цена'
        )
    
    discount=models.DecimalField(
        default=0.00, 
        max_digits=7, 
        decimal_places=2,
        verbose_name='Скидка в %'
        )
    # PositiveItegerFiel - Поле, которое определяет положительные целые числа.
    quantity=models.PositiveIntegerField(
        default=0,
        verbose_name='Количество'
        )
    
    # ForeignKey - Поле, которое ссылается на модель, определенную в параметре "to"
    # Данное поле позволяет связать данные классы связью "Один ко многим"
    # т.е. Одна модель Categories может вмещать в себя бессчисленное количество моделей 
    # Products 
    category=models.ForeignKey(
        to=Categories, 
        on_delete=models.CASCADE
        )
    # Класс Meta - позволяет переопределять отображение в интерфейсе базы данных и админ.панеле
    # Некоторые поля
    class Meta:
        db_table='product'
        verbose_name='Продукт'
        verbose_name_plural='Продукты'
        # ordering - параметр, по которому Django сортирует модели в админ панеле
        ordering = ("id", )

    def __str__(self):
        return self.name 
    
    # def display_id(self):
    #     return f"{self.id:05}"
    
    # def sell_price(self):
    #     if self.discount:
    #         return round(self.price - self.price*self.discount/100, 2)
        
    #     return self.price
# Create your models here.