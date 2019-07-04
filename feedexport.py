"""
The standard CSVItemExporter class does not pass the kwargs through to the
CSV writer, resulting in EXPORT_FIELDS and EXPORT_ENCODING being ignored
(EXPORT_EMPTY is not used by CSV).
"""
import csv
from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

class CSVkwItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['delimiter'] = settings.get('CSV_DELIMITER') or "\t"
        kwargs['quotechar'] = settings.get('CSV_QUOTECHAR') or "\""
        kwargs['quoting'] = csv.QUOTE_ALL
        kwargs['fields_to_export'] = settings.getlist('EXPORT_FIELDS') or None
        kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8')

        super(CSVkwItemExporter, self).__init__(*args, **kwargs)


class CSVkwCommentItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['delimiter'] = settings.get('CSV_DELIMITER') or "\t"
        kwargs['quotechar'] = settings.get('CSV_QUOTECHAR') or "\""
        kwargs['quoting'] = csv.QUOTE_ALL
        kwargs['fields_to_export'] = settings.getlist('COMMENT_EXPORT_FIELDS') or None
        kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8')

        super(CSVkwCommentItemExporter, self).__init__(*args, **kwargs)
