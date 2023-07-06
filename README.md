# kfc_test
## Тестовое задание 1 для OMD OM Group // Junior Python Developer

Были проанализированы запросы страницы https://www.kfc.ru/restaurants

Далее я нашел запрос POST
	https://api.kfc.digital/api/store/v2/store.geo_search

 Тело запроса имеет параметры "coordinates","radiusMeters","channel","showClosed"

 "coordinates" определяет центр круга, "radiusMeters" определяет радиус, "showClosed" определяет видимость закрытых предприятий

 Далее по картам определил примерный центр и радиус покрывающий рестораны в Новосибирске

 Определил необходимые заголовки для работы запроса

 Написал скрипт [main.py](https://github.com/shinkared/kfc_test/blob/master/main.py) который посылает запрос и получает список ресторанов в заданом круге, в файле [result.json](https://github.com/shinkared/kfc_test/blob/master/result.json) есть пример описания ресторана

 Скрипт обрабатывает данные и записывает их в [kfc.db](https://github.com/shinkared/kfc_test/blob/master/kfc.db)

 В файле [query](https://github.com/shinkared/kfc_test/blob/master/query) можно найти запрос для аналитика
```sql:
SELECT *
FROM kfc_nsk
WHERE breakfastStartTime <= '08:45:00' AND breakfastEndTime > '08:45:00' and city='Новосибирск';
```
