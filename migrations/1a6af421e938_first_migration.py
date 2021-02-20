"""First migration

Migration ID: 1a6af421e938
Revises: 
Creation Date: 2021-02-19 15:38:56.378414

"""

from weppy.orm import migrations


class Migration(migrations.Migration):
    revision = '1a6af421e938'
    revises = None

    def up(self):
        self.create_table(
            'readings',
            migrations.Column('id', 'id'),
            migrations.Column('station_id', 'text'),
            migrations.Column('date', 'text'),
            migrations.Column('temperature', 'float'))

    def down(self):
        self.drop_table('readings')