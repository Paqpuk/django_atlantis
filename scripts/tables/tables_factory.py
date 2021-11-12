from django_tables2.tables import Table


def table_factory(model, table=Table, fields=None, exclude=None, localize=None, parent_meta=None, extra_columns=None):
    """
    Return Table class for given `model`, equivalent to defining a custom table class::

        class MyTable(tables.Table):
            class Meta:
                model = model

    Arguments:
        :param model: (`~django.db.models.Model`): Model associated with the new table
        :param table: (`.Table`): Base Table class used to create the new one
        :param fields: (list of str): Fields displayed in tables
        :param exclude: (list of str): Fields exclude in tables
        :param localize: (list of str): Fields to localize
        :param parent_meta:
        :param extra_columns: extra column class from extra_column.py
    """
    attrs = {"model": model}
    if fields is not None:
        attrs["fields"] = fields
    if exclude is not None:
        attrs["exclude"] = exclude
    if localize is not None:
        attrs["localize"] = localize
    # If parent form class already has an inner Meta, the Meta we're
    # creating needs to inherit from the parent's inner meta.
    if not parent_meta:
        parent = (table.Meta, object) if hasattr(table, "Meta") else (object,)
    else:
        setattr(parent_meta, 'fields', ['name', 'responsible', 'Delete', 'Add', 'station'])
        parent = (parent_meta, )

    meta = type("Meta", parent, attrs)
    # define extra columns class which
    if extra_columns:
        extra_col_class = type('buttons', (Table, ), {str(cls()): cls.accessor for cls in extra_columns})
        for cls in extra_columns:
            setattr(extra_col_class, f'render_{str(cls())}', staticmethod(cls.render_accessor))
        bases = (extra_col_class, table)
    else:
        bases = (table, )

    # Give this new table class a reasonable name.
    class_name = model.__name__ + "AutogeneratedTable"
    # Class attributes for the new table class.
    table_class_attrs = {"Meta": meta}
    return type(table)(class_name, bases, table_class_attrs)
