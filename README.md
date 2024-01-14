# Проект автоматизации тестирования API restful-booker.

## Краткое описание.
Проект содержит автотесты на api [restful-booker](https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-UpdateBooking). 

API тесты реализованы в связке `Python`+`Requests`.  
Запуск тестов осуществляется в `Jenkins`.  
Для отчетов по результатам прогона используется `Allure` + отправляется уведомление в телеграм с краткими результатами.

## Что покрыто тестами
- получение информации о бронировании по id
- healthcheck проверка
- создание бронирования
- удаление бронирования
- изменение существующего бронирования

## Технологии.
<img src="resources/icons/python-original.svg" width="50"> <img src="resources/icons/pytest-original-wordmark.svg" width="50">
<img src="resources/icons/jenkins.png" width="50">
<img src="resources/icons/allure_report.png" width="50">
<img src="resources/icons/allure_testops.png" width="50"> <img src="resources/icons/tg.png" width="50">

## Запуск на сервере.

Запуск тестов выполняется в проекте [Jenkins](https://jenkins.autotests.cloud/job/008-Bryazgin-api_diploma/).

### 1. Перейти в [проект](https://jenkins.autotests.cloud/job/008-Bryazgin-api_diploma/) и нажать кнопку `Build with Parameters`.
<img src="resources/screenshots/Build with Parameters.png" width="1000">

### 2. Указать параметры сборки и нажать кнопку `Build`
`COMMENT` - комментарий, указывающий особенности сборки  
`ENVIRONMENT` - выбор среды запуска тестов  
<img src="resources/screenshots/select parameters.png" width="1000">

### 3. Дождаться окончания прогона
<img src="resources/screenshots/finish run.png" width="1000"> 

### 4. Для просмотра отчета нажать одну из иконок 
<img src="resources/screenshots/report icons.png" width="1000"> 

### Пример отчета в Allure
<img src="resources/screenshots/Allure.png" width="1000">

### Пример дэшборда в Allure testops
<img src="resources/screenshots/Allure Testops.png" width="1000">


### По результатам прогона получаем уведомление с краткой информацией в телеграм
<p align="center"> 
    <img src="resources/screenshots/telegram.png" width="400">
</p>