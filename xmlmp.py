# Импортирование библиотек
import xml.etree.ElementTree as ET  # Библиотека для обработки XML-структур
from datetime import datetime       # Библиотека для работы со временем

# Создание корневого элемента <rss>
rss = ET.Element("rss")             # Создание корневого элемента XML-структуры
rss.set("xmlns:dc", "http://purl.org/dc/elements/1.1/")  # Добавление атрибута xmlns:dc
rss.set("version", "2.0")           # Добавление атрибута version

# Создание элемента <channel>
# Этот элемент представляет канал, который содержит информацию о фиде
channel = ET.SubElement(rss, "channel")

# Добавление дочерних элементов для <channel>
# Этот блок кода добавляет главную информацию о фиде

# Вставьте сюда заголовок вашего фида
title = ET.SubElement(channel, "title")         # Добавление элемента <title>
title.text = "Example RSS Feed"                 # Добавление текста внутри элемента <title>

# Вставьте сюда ссылку на ваш фид
link = ET.SubElement(channel, "link")           # Добавление элемента <link>
link.text = "http://www.example.com/"           # Добавление текста внутри элемента <link>

# Вставьте сюда описание вашего фида
description = ET.SubElement(channel, "description")  # Добавление элемента <description>
description.text = "An example RSS feed"        # Добавление текста внутри элемента <description>

# Вставьте сюда язык вашего фида
language = ET.SubElement(channel, "language")   # Добавление элемента <language>
language.text = "en-us"                         # Добавление текста внутри элемента <language>

# Добавление времени публикации. Если не нужно, можно удалить
pubDate = ET.SubElement(channel, "pubDate")     # Добавление элемента <pubDate>
pubDate.text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")  # Добавление текста с текущим временем внутри элемента <pubDate>

# Создание элемента <item> для статей в фиде
# Этот блок кода добавляет информацию о статье внутри фида
item = ET.SubElement(channel, "item")           # Добавление элемента <item>

# Вставьте сюда заголовок вашей статьи
title = ET.SubElement(item, "title")            # Добавление элемента <title>
title.text = "Example article"                  # Добавление текста внутри элемента <title>

# Вставьте сюда ссылку на вашу статью
link = ET.SubElement(item, "link")              # Добавление элемента <link>
link.text = "http://www.example.com/articles/article1"  # Добавление текста внутри элемента <link>

# Вставьте сюда описание вашей статьи
description = ET.SubElement(item, "description") # Добавление элемента <description>
description.text = "An example article description"  # Добавление текста внутри элемента <description>

# Вставьте сюда имя автора вашей статьи
dc = ET.SubElement(item, "dc:creator")           # Добавление элемента <dc:creator>
dc.text = "John Doe"                            # Добавление текста внутри элемента <dc:creator>

# Вставьте сюда время публикации вашей статьи. Если не нужно, можно удалить
pubDate = ET.SubElement(item, "pubDate")        # Добавление элемента <pubDate>
pubDate.text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z") # Добавление текста с текущим временем внутри элемента <pubDate>

# Сериализация XML дерева в строку
# Этот блок кода конвертирует XML-структуру в строку, чтобы ее можно было вывести на экран или использовать в других целях
xml_str = ET.tostring(rss)

# Вывод XML строки в консоль
# Этот блок кода выводит полученную XML-строку на экран
print(xml_str.decode())