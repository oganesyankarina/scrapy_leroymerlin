scrapy_leroymerlin

1)Взять любую категорию товаров на сайте Леруа Мерлен(еще лучше - использовать input и конструктор паука). Собрать с использованием ItemLoader следующие данные:
● название;
● все фото;
● параметры товара в объявлении(не часть HTML!);
● ссылка;
● цена.
С использованием output_processor и input_processor реализовать очистку и преобразование данных. Цены должны быть в виде числового значения.
С сохранением в MongoDB!
Без дубликатов!

2)Написать универсальный обработчик характеристик товаров, который будет формировать данные вне зависимости от их типа и количества.

3)Реализовать хранение скачиваемых файлов в отдельных папках, каждая из которых должна соответствовать собираемому товару
