from bam_masterdata.datamodel.object_types import Chemical, Instrument
from bam_masterdata.parsing import AbstractParser


class MasterdataParserExample(AbstractParser):
    def parse(self, files, collection, logger):
        chemical = Chemical(
            name="Example Chemical",
            manufacturer="Example Manufacturer",
            hazardous_substance=False,
            bam_oe="OE_VP.1",
            bam_location_complete="UE_08_0_101",
        )
        chemical_id = collection.add(chemical)
        instrument = Instrument(
            name="Example Instrument",
            manufacturer="Example Manufacturer",
            bam_oe="OE_VP.1",
            bam_location_complete="UE_08_0_101",
        )
        instrument_id = collection.add(instrument)
        _ = collection.add_relationship(chemical_id, instrument_id)
        logger.info("Parsing finished: Added example chemical and instrument.")


from bam_masterdata.logger import logger
from bam_masterdata.metadata.entities import CollectionType

collection = CollectionType()
files = []
parser = MasterdataParserExample()


parser.parse(files, collection, logger)
