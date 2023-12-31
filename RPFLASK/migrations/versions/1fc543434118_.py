"""empty message

Revision ID: 1fc543434118
Revises: 
Create Date: 2023-11-05 16:27:26.047619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fc543434118'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('autor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('libro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=120), nullable=False),
    sa.Column('autor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['autor_id'], ['autor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prestamo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('libro_id', sa.Integer(), nullable=False),
    sa.Column('fecha_prestamo', sa.Date(), nullable=False),
    sa.Column('fecha_devolucion', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['libro_id'], ['libro.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prestamo')
    op.drop_table('libro')
    op.drop_table('usuario')
    op.drop_table('autor')
    # ### end Alembic commands ###
