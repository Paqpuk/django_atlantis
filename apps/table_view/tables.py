from .models import HILs
from scripts.tables.tables_factory import table_factory
from scripts.tables.extra_columns import Delete, Add
from scripts.tables.themes import Atlantis


HILsTable = table_factory(HILs, parent_meta=Atlantis, extra_columns=[Delete, Add])
