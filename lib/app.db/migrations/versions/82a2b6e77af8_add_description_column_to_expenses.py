"""Add description column to expenses

Revision ID: 82a2b6e77af8
Revises: b927f227d323
Create Date: 2025-05-28 15:35:33.101514

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82a2b6e77af8'
down_revision: Union[str, None] = 'b927f227d323'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # Remove creation of tables that already exist
    # Skip adding columns that already exist to avoid duplicate column error
    # op.add_column('expenses', sa.Column('description', sa.String(), nullable=True))
    # op.add_column('expenses', sa.Column('date', sa.Date(), nullable=True))
    # op.add_column('expenses', sa.Column('created_at', sa.DateTime(timezone=True), nullable=True))
    # op.add_column('expenses', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))
    # op.add_column('expenses', sa.Column('user_id', sa.Integer(), nullable=True))
    # op.add_column('expenses', sa.Column('category_id', sa.Integer(), nullable=True))
    # SQLite does not support ALTER COLUMN, so skip this step
    # op.alter_column('expenses', 'amount',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.Float(),
    #            nullable=False)
    # SQLite does not support ALTER CONSTRAINT, so skip foreign key creation
    # op.create_foreign_key(None, 'expenses', 'users', ['user_id'], ['id'])
    # op.create_foreign_key(None, 'expenses', 'categories', ['category_id'], ['id'])
    op.drop_column('expenses', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('expenses', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'expenses', type_='foreignkey')
    op.drop_constraint(None, 'expenses', type_='foreignkey')
    op.alter_column('expenses', 'amount',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               nullable=True)
    op.drop_column('expenses', 'category_id')
    op.drop_column('expenses', 'user_id')
    op.drop_column('expenses', 'updated_at')
    op.drop_column('expenses', 'created_at')
    op.drop_column('expenses', 'date')
    op.drop_column('expenses', 'description')
    op.drop_table('totals')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###
