import dataclasses
from dataclasses import dataclass
from Bio import Seq, SeqRecord

import util.coordinates as coords
import util.wrappers as wrappers

@dataclass
class ReferenceIndex:
    value: int


@dataclass
class AlignedSequence:
    this: Seq
    reference: Seq
    alignment: (str, str) = dataclasses.field(default=None)
    coordinates_mapping: list[int] = dataclasses.field(default=None)


    def get_alignment(self):
        if not self.alignment:
            self.alignment = wrappers.mafft([self.reference, self.this])

        return self.alignment


    def aligned_reference(self):
        return self.get_alignment()[0]


    def aligned_this(self):
        return self.get_alignment()[1]


    def map_index(self, index):
        if not self.coordinates_mapping:
            self.coordinates_mapping = coords.map_positions(self.aligned_reference(), self.aligned_this())

        if not isinstance(index, int):
            raise TypeError(f"Expected integer as index", index)

        return self.coordinates_mapping[index]


    def index(self, index):
        if isinstance(index, ReferenceIndex):
            index = self.map_index(index)

        return self.this[index]


    def slice(self, first, last):
        if isinstance(first, ReferenceIndex):
            first = self.map_index(first)
        if isinstance(last, ReferenceIndex):
            last = self.map_index(last)

        newthis = self.this[first:(last + 1)]
        newreference = self.reference[self.map_index(first):(self.map_index(last) + 1)]
        # TODO: calculate new "coordinates_mapping" and new "alignment" from these indexes.
        return Sequence(this=newthis, reference=newreference)


    def reverse(self):
        newthis = SeqRecord.SeqRecord(Seq.reverse_complement(this.seq),
                                      id = this.id + " [REVERSED]",
                                      name = this.name
                                      )

        return Sequence(this=newthis, reference=self.reference)
