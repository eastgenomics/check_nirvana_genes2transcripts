This script is used to check that all transcripts present in genes2transcripts are available in Nirvana RefSeq annotation cache.

Example input files are provided to demonstrate success / failure

```
Usage:
nirvana_tx_check.py genes2transcripts_filepath nirvana_refseq_cache_filepath
```

```
e.g.
nirvana_tx_check.py test_files/g2t_test_failure Cache/26/GRCh37/GRCh37_RefSeq_26.gff.gz
NM_015665.5     Present
NM_001127448.1  Present
NM_020745.3     Present
NM_000014.4     Present
NM_005502.7     Absent
NM_017436.4     Present
NM_005763.3     Present
NM_999999.9     Absent
NM_173076.2     Present
NM_001605.2     Present

Missing:
NM_999999.9
NM_005502.7

FAILED
```
