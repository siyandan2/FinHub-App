"""empty message

Revision ID: 3fa4da86c560
Revises: 0fdd11599881
Create Date: 2024-03-12 03:53:51.920406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fa4da86c560'
down_revision = '0fdd11599881'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('applications', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_doc_link', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('matric_doc_link', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('academic_doc_link', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('unemployed_doc_link', sa.String(length=150), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('applications', schema=None) as batch_op:
        batch_op.drop_column('unemployed_doc_link')
        batch_op.drop_column('academic_doc_link')
        batch_op.drop_column('matric_doc_link')
        batch_op.drop_column('id_doc_link')

    # ### end Alembic commands ###