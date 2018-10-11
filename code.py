import psycopg2


def most_popular_three_articles():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("select articles.title, count(log.path) as views "
                   "from articles join log "
                   "on articles.slug = substr(log.path,10) "
                   "group by articles.title "
                   "order by views desc "
                   "limit 3; ")
    result = cursor.fetchall()
    print(result)
    db.close()


def most_popular_authors():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("select authors.name, count(*) as views "
                   "from articles, authors, log "
                   "where articles.slug = substr(log.path,10) "
                   "and articles.author = authors.id "
                   "group by authors.name "
                   "order by views desc;")
    result = cursor.fetchall()
    print(result)
    db.close()


def percentageerror():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("create view error_num as "
                   "select cast(time as date),count(*) as error from log "
                   "where status = '404 NOT FOUND' "
                   "group by cast(time as date); "
                   "create view total_num as "
                   "select cast(time as date),count(*) as total from log "
                   "group by cast(time as date); "
                   "select error_num.time, "
                   "round(error_num.error * 100.0/total_num.total, 1) "
                   "as percentage "
                   "from error_num, total_num "
                   "where error_num.time = total_num.time "
                   "order by percentage desc; "
                   )
    result = cursor.fetchall()
    print(result)
    db.close()


most_popular_authors()
most_popular_three_articles()
percentageerror()
