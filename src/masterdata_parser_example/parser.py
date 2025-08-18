from bam_masterdata.datamodel.object_types import Instrument, Storage
from bam_masterdata.parsing import AbstractParser


class MasterdataParserExample(AbstractParser):
    def parse(self, files, collection, logger):
        storage = Storage(
            name="Example Storage",
            storage_storage_validation_level="BOX",
        )
        storage_id = collection.add(storage)
        instrument = Instrument(
            name="Example Instrument",
            manufacturer="Example Manufacturer",
            bam_oe="OE_VP.1",
            bam_location_complete="UE_08_0_101",
        )
        instrument_id = collection.add(instrument)
        _ = collection.add_relationship(storage_id, instrument_id)
        logger.info("Parsing finished: Added example chemical and instrument.")
