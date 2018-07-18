# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sqlalchemy as sa

from h.db import Base
from h.db import mixins
from h import pubid

ORGANIZATION_DEFAULT_PUBID = '__default__'


class Organization(Base, mixins.Timestamps):
    __tablename__ = 'organization'

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)

    # We don't expose the integer PK to the world, so we generate a short
    # random string to use as the publicly visible ID.
    pubid = sa.Column(sa.Text(),
                      default=pubid.generate,
                      unique=True,
                      nullable=False)

    name = sa.Column(sa.UnicodeText(), nullable=False, index=True)

    logo = sa.Column(sa.UnicodeText())

    authority = sa.Column(sa.UnicodeText(), nullable=False)

    def __repr__(self):
        return '<Organization: %s>' % self.pubid

    @classmethod
    def default(cls, session):
        return session.query(cls).filter_by(pubid=ORGANIZATION_DEFAULT_PUBID).one()
