# Number of patches

1. The benchmark being ran apoa1, has 144 patches, ideally the number of processors
    should be equal to number of patches + 1, but since we do not have enough
    processors for this, we should use as many processors as available 
    (at least for single node)

2. Restrict the number of processors used for PME by setting PMEProcessors
    to half the number of processors being used.

