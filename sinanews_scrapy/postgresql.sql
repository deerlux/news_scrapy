create table if not exists news_data (
    id serial primary key,
    title varchar(160),
    source varchar(40),
    public_time timestamp,
    body text,
    crawl_time timestamp,
    url varchar(160),
    keywords varchar(40),
    domain varchar(60)
);

--

--create table if not exists keywords (
--    news_id int primary key references news_data(id),
--    keywords varchar(40)
--);

--create table if not exists news_domain (
--    news_id int primary key references news_data(id),
--    domain varchar(60)
--);

--create view news_view as
--    select news_data.id, title, 
--    source, public_time, crawl_time, 
--    url, keywords, domain, news_data.body 
--    from news_data, keywords, news_domain
--    where news_data.id = keywords.news_id 
--    and news_data.id = news_domain.news_id;

create index news_data_title_idx on news_data(title);
create index news_data_pulic_time_idx on news_data(public_time);
create index news_data_crawl_time_idx on news_data(crawl_time);
create index news_data_keywords_idx on news_data(keywords);
create index news_data_domain_idx on news_data(domain);



