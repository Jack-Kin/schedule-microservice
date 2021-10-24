from application_services.BaseApplicationResource import BaseRDBApplicationResource
import database_services.RDBService as d_service


class ScheduleResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def get_data_resource_info(cls):
        return 'hw1_db', 'schedule'

    @classmethod
    def get_by_schedule_id(cls, scheduledId):
        res = d_service.RDBService.get_by_prefix("hw1_db", "schedule", "scheduledId", scheduledId)
        return res

    @classmethod
    def get_by_owner_id(cls, ownerId):
        res = d_service.RDBService.get_by_prefix("hw1_db", "schedule", "ownerId", ownerId)
        return res

    @classmethod
    def create_schedule(cls, schedule_data):
        res = d_service.RDBService.create("hw1_db", "schedule", schedule_data)
        return res

    @classmethod
    def delete(cls, scheduleId):
        res = d_service.RDBService.delete("hw1_db", "schedule", scheduleId)
        return res

    @classmethod
    def update(cls, scheduleId, row):
        res = d_service.RDBService.update("hw1_db", "schedule", scheduleId, row)