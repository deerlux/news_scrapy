create table if not exists news_data (
    id serial primary key,
    title varchar(160),
    source varchar(40),
    public_time timestamp,
    body text,
    crawl_time timestamp
);

create table if not exists keywords (
    id serial primary key,
    news_id int references news_data(id),
    keyword varchar(40)
);

create table if not exists news_domain (
    id serial primary key,
    news_id int references news_data(id),
    domain varchar(60)
);

create index news_data_title_idx on news_data(title);
create index news_data_pulic_time_idx on news_data(public_time);
create index news_data_crawl_time_idx on news_data(crawl_time);
create index keywords_keyword_idx on keywords(keyword);
create index news_domain_domain_idx on news_domain(domain);



