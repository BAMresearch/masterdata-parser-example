from bam_masterdata.datamodel.object_types import Instrument
from bam_masterdata.parsing import AbstractParser


class MasterdataParserExample(AbstractParser):
    def parse(self, files, collection, logger):
        instrument_input = Instrument(
            name="Example Input Instrument",
            manufacturer="Example Manufacturer",
            bam_oe="OE_VP.1",
            bam_location_complete="UE_08_0_101",
        )
        instrument_input_id = collection.add(instrument_input)
        instrument_output = Instrument(
            name="Example Output Instrument",
            manufacturer="Example Manufacturer",
            bam_oe="OE_VP.1",
            bam_location_complete="UE_08_0_101",
        )
        instrument_output_id = collection.add(instrument_output)
        _ = collection.add_relationship(instrument_input_id, instrument_output_id)
        logger.info(
            "Parsing finished: Added examples input and output instruments and their relation."
        )
