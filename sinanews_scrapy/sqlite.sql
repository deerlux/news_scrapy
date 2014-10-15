CREATE TABLE IF NOT EXISTS news_data (
    id INTEGER PRIMARY KEY ,
    title, 
    source, 
    public_time, 
    body, 
    crawl_time,
    url,
    keywords, 
    domain);
CREATE INDEX IF NOT EXISTS title_idx on news_data(title);
CREATE INDEX IF NOT EXISTS crawltime_idx on news_data(crawl_time);

