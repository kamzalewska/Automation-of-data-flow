DROP table IF EXISTS results;
CREATE table IF NOT EXISTS kairomones.results
    (
    id int not null,
    regime varchar(255) not null,
    line int not null check (line between 1 and 10),
    trial int not null check (line between 1 and 10),
    start_plant varchar(255) not null,
    kairomone_source varchar(255) not null,
    start_numb int not null check (line between 1 and 10),
    end_numb int not null check (line between 1 and 10)
                                )

