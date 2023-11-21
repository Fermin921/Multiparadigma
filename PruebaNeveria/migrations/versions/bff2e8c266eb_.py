"""empty message

Revision ID: bff2e8c266eb
Revises: 
Create Date: 2023-11-19 14:03:45.791075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bff2e8c266eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoria',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('sucursal',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=False),
    sa.Column('direccion', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('direccion'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cliente',
    sa.Column('nombre_empresa', sa.String(length=50), nullable=False),
    sa.Column('direccion', sa.String(length=255), nullable=False),
    sa.Column('fecha_registro', sa.DateTime(), nullable=False),
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursal.id'], ),
    sa.PrimaryKeyConstraint('nombre_empresa')
    )
    op.create_table('empleado',
    sa.Column('clave', sa.String(length=50), nullable=False),
    sa.Column('rfc', sa.String(length=255), nullable=False),
    sa.Column('nombres', sa.String(length=255), nullable=False),
    sa.Column('apellidos', sa.String(length=255), nullable=False),
    sa.Column('fecha_nacimiento', sa.DateTime(), nullable=False),
    sa.Column('edad', sa.Integer(), nullable=False),
    sa.Column('sueldo', sa.Float(), nullable=False),
    sa.Column('area_laboral', sa.String(length=50), nullable=False),
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursal.id'], ),
    sa.PrimaryKeyConstraint('clave'),
    sa.UniqueConstraint('rfc')
    )
    op.create_table('materiaprima',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('precio_unitario', sa.Float(), nullable=False),
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursal.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producto',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sabor', sa.String(length=255), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categoria.id'], ),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursal.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sabor')
    )
    op.create_table('proveedor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=False),
    sa.Column('apellido', sa.String(length=255), nullable=False),
    sa.Column('direccion', sa.String(length=255), nullable=False),
    sa.Column('telefono', sa.String(length=10), nullable=False),
    sa.Column('nombre_empresa', sa.String(length=50), nullable=False),
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursal.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('telefono',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('no_tel', sa.String(length=10), nullable=False),
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursal.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('encargo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre_encargo', sa.String(length=255), nullable=False),
    sa.Column('cantidad_encargo', sa.Integer(), nullable=False),
    sa.Column('cantidad_a_pagar', sa.Float(), nullable=False),
    sa.Column('forma_de_pago', sa.String(length=255), nullable=False),
    sa.Column('fecha_encargo', sa.DateTime(), nullable=False),
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.Column('proveedor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['proveedor_id'], ['proveedor.id'], ),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursal.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venta',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fecha_venta', sa.DateTime(), nullable=False),
    sa.Column('monto_total', sa.Float(), nullable=False),
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.Column('empleado_clave', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['empleado_clave'], ['empleado.clave'], ),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursal.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('productosvendidos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('venta_id', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.ForeignKeyConstraint(['venta_id'], ['venta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productosvendidos')
    op.drop_table('venta')
    op.drop_table('encargo')
    op.drop_table('telefono')
    op.drop_table('proveedor')
    op.drop_table('producto')
    op.drop_table('materiaprima')
    op.drop_table('empleado')
    op.drop_table('cliente')
    op.drop_table('users')
    op.drop_table('sucursal')
    op.drop_table('categoria')
    # ### end Alembic commands ###