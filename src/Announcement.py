'''
        Announcement module is created by the sake of abstraction.
        I write about this abstraction in mongo/AnnouncementDatabase
'''



from mongo import AnnouncementDatabase
from Logging import logger


def find(department_id):
    return AnnouncementDatabase.find(department_id)


def update(department_id, announcements):
    AnnouncementDatabase.update(department_id, announcements)
    logger.info(f"Announcements updated for {department_id} department in database!")


def new_department(department_id):
    document = {
        'department': department_id,
        'announcements': []
    }

    AnnouncementDatabase.insert_documents([document])
    logger.info('New document(s) have been inserted!')


def compare(olds, news):
    diff = []

    for announcement in news:
        if announcement not in olds:
            diff.append(announcement)

    return diff
    
