create table content
(
    contentId      	  		int	               	not null		auto_increment,
	restaurantId      		varchar(100)                        null,
	restaurantName    		varchar(100)                        null,
	restaurantImageUrls		varchar(100)                        null,
    restaurantType			varchar(100)                        null,
    restaurantDescription	varchar(100)                        null,
    restaurantArea			varchar(100)                        null,
    restaurantLoc			varchar(100)                        null,
    score					int			                        null,
	PRIMARY KEY (contentId)
);