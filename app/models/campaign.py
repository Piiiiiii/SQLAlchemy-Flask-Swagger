from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base


class Campaign(Base):
    __tablename__ = 'campaign'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # TODO: list campaign table schema here
    user_id = Column(UUID)
    token = Column(String)
    campaign_name = Column(String)
    # campaign_obj_type =
    # campaign_timeline =
    # campaign_core_metric =

    def keys(self):
        self.hide('user_id')
        return self.fields

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
