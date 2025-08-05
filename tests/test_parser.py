from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities import CollectionType


class TestMasterdataParserExample:
    def test_parse(self, parser):
        collection = CollectionType()
        parser.parse([], collection, logger)

        assert len(collection.objects) == 2
        objects = list(collection.objects.values())
        assert objects[0].name == "Example Chemical"
        assert objects[1].name == "Example Instrument"
        assert len(collection.relationships) == 1
