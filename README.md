# schedule-microservice

## Database Design

DynamoDB is used in this microservice. DynamoDB is a schemaelss database. It has greater flexibility over data types, and it has no pre-defined database schemas, allowing it to grow and change as your data-driven operations change and mature.



```json
{
    scheduleId (key)
    scheduleTitle
    targetArea
    revisedTimeStamp (int)
    OwnerId
    EditorIds: [
    	"aaaaaaaaaa",
    	"bbbbbbbbbb"
    ]
    scheduleType: PRESELECT, EDITING, COMPLETED    1/ 3
    ScheduleContents: [
        {
            restaurantId
            restaurantName
            restaurantImageUrls
            restaurantType
            restaurantDescription
            restaurantArea
            restaurantLoc:{
            lat:
            Ing:
        	}
        	score
        }
    ......
    ]
}
```



## API Design

```
GET /schedule: retrieve the schedule list by user id
	pageNo [string] (query parameter)
	pageSize [string] (query parameter)

POST /schedule: create a preselected type schedule
	userId
	targetArea
	scheduleTitle
	
GET /schedule/{scheduleId}: retrieve a schedule
	scheduleId (path) required
	
POST /schedule/{scheduleId}: update a schedule
	scheduleId [string] (path) required
	EditingSchedule [object] (body) required
	
DELETE /schedule/{scheduleId}: delete a schedule
	scheduleId [string] (path) required

GET schedule/{scheduleId}/restaurant/{restaurantId}: retrieve a like info of a specific restaurant in the schedule
	scheduleId [string] (path) required
	restaurantId [string] (path) required

PUT　schedule/{scheduleId}/restaurant/{restaurantId}:　initialize a like info of a specific restaurant in the schedule
	scheduleId [string] (path) required
	restaurantId [string] (path) required

DELETE schedule/{scheduleId}/restaurant/{restaurantId}: delete a like info of a specific restaurant in the schedule 
	scheduleId [string] (path) required
	restaurantId [string] (path) required

GET /schedule/{scheduleId}/submit: change the stage of the schedule from  to COMPLETED

GET /schedule/{scheduleId}/finish: change the stage of the schedule from EDITING to COMPLETED
	scheduleId [string] (path) required
```





## Docker Configuration

Docker installation on AWS:

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html

Dockerfile:

```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "./app.py", "--host=0.0.0.0:5003"]
```

Build docker image
```bash
docker build --tag schedule-test .
```

Run image as container
```bash
docker run --publish 5003:5003 schedule-test
```
