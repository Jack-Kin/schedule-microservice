create table schedule
(
    scheduledId    int                        	not null		AUTO_INCREMENT,
    contentId      int	                      	not null,
    scheduledTitle varchar(100)               	null,
    revisedTime    timestamp default CURRENT_TIMESTAMP not null,
    targetArea     varchar(100)               	null,
    ownerId        int                        	not null,
    editorIds      int                        	null,
    scheduleType   varchar(100)   			  	null,
	CONSTRAINT scheduleContent PRIMARY KEY (scheduledId, contentId)
);
show tables;