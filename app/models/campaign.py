from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Date, Float
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import re

from app.models.base import Base, db
from app.models.user import User

campaign_editorial_topic = db.Table('campaign_editorial_topic',
              Column('campaign_id', Integer, ForeignKey('campaign.campaign_id')),
              Column('editorial_topic_id', Integer, ForeignKey('editorial_topic.editorial_topic_id')),
              )


class Campaign(Base):
    __tablename__ = 'campaign'
    index = Column(Integer, primary_key=True, autoincrement=True)
    # TODO: list campaign table schema here
    # user_id = Column(UUID)
    # token = Column(String)
    campaign_id = Column(Integer, unique=True)
    campaign_name = Column(String)
    campaign_obj_type = Column(Enum('私域促活/留存', '私域拉新', '裂变', name='campaign objective type'))
    campaign_time_start = Column(Date)
    campaign_time_end = Column(Date)
    campaign_core_metric_type = Column(String)
    campaign_core_metric_value = Column(Float)
    editorial_topics = db.relationship('Editorial_topic', secondary=campaign_editorial_topic,
                                       backref=db.backref('campaigns', lazy='dynamic'))

    def keys(self):
        self.hide('index')
        return self.fields

    @staticmethod
    def create_campaign(user_id, campaign_id, campaign_name, campaign_obj_type, campaign_time_start, campaign_time_end):
        date_number_start = list(map(int, re.compile(r'\d+').findall(campaign_time_start)))
        date_number_end = list(map(int, re.compile(r'\d+').findall(campaign_time_end)))
        campaign_time_start = datetime(date_number_start[0], date_number_start[1], date_number_start[2])
        campaign_time_end = datetime(date_number_end[0], date_number_end[1], date_number_end[2])
        with db.auto_commit():
            new_campaign = Campaign(campaign_id=campaign_id, campaign_name=campaign_name, campaign_obj_type=campaign_obj_type,
                                    campaign_time_start=campaign_time_start, campaign_time_end=campaign_time_end)
            linked_user = User.query.filter_by(user_id=user_id).first_or_404()
            new_campaign.users.append(linked_user)
            db.session.add(new_campaign)
        return linked_user

    @classmethod
    def get_campaigns(cls, page=1, size=15):
        paginator = Campaign.query.paginate(
            page=page,
            per_page=size,
            error_out=True
        )

        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }

    @classmethod
    def get_campaigns_by_user_token(cls, user_id, token, page=1, size=15):
        paginator = Campaign.query.filter_by(
            user_id=user_id,
            token=token
        ).paginate(
            page=page,
            per_page=size,
            error_out=True
        )

        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }
