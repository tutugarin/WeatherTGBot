# TelegramBot
This is a homework task for Missing Semester

1. Ершов Иван Петрович
2. * Бот работает `inline`, при вызове может дать погоду в указанном после ника городе (по умолчанию в Москве). Город можно указывать как на английском, так и на русском языке. Бот говорит температуру, температуру по ощущениям, скорость ветра с его напревлением, осадки и давление.
   * Юзернейм бота - `@FairBoobSize_bot`.
   * "Boob" созвочну с "буб", что является сокращением слова "бубен". Как известно индейцы бьют в бубен, чтобы вызывать нужную погоду. Вызывать нужную погоду я не       умею, но мой бот знает размер точный размер бубна, в который били сегодня индейцы, и по этим данным говорит погоду.
3. Amazon
4. Использовал `WatchTower` (`docker-compose.yml` находится в репозитории). При каждом `push` в репозиторий происходит проверка кода на код-стайл и на отсутствие ошибок при помощи `pylint`. При каждом `release` или добавлении нового тэга происходит аналогичный `job`, что и при `push`, но в данном случае при успешном прохождении тестрования также проиходит `docker push`, что влечет за собой перезапуск бота на сервере.
