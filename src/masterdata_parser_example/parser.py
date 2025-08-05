from bam_masterdata.datamodel.object_types import Chemical, Instrument
from bam_masterdata.parsing import AbstractParser


class MasterdataParserExample(AbstractParser):
    def parse(self, files, collection, logger):
        chemical = Chemical(name="Example Chemical")
        chemical_id = collection.add(chemical)
        instrument = Instrument(name="Example Instrument")
        instrument_id = collection.add(instrument)
        _ = collection.add_relationship(chemical_id, instrument_id)
        logger.info("Parsing finished: Added example chemical and instrument.")
