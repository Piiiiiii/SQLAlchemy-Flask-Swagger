from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base, db
# from app.models.campaign import Campaign

# If a table exists, create_all will not update the changed table. So you should delete this table first.

user_campaign = db.Table('user_campaign',
              Column('user_id', Integer, ForeignKey('user_table.user_id')),
              Column('campaign_id', Integer, ForeignKey('campaign.campaign_id')),
              )


# user is a keyword for pqsql
class User(Base):
    __tablename__ = 'user_table'
    index = Column(Integer, primary_key=True, autoincrement=True)
    # TODO: list campaign table schema here
    user_id = Column(Integer, unique=True)
    campaigns = db.relationship('Campaign', secondary=user_campaign, backref=db.backref('users', lazy='dynamic'))

    def keys(self):
        self.hide('id')
        return self.fields

    @staticmethod
    def create_user(user_id):
        with db.auto_commit():
            new_user = User(user_id=user_id)
            db.session.add(new_user)
        return 'create user success'
