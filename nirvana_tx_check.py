import sys
import gzip

def get_nirvana_tx_list(nirvana_gff):
    """
    Extract a list of transcripts from a Nirvana RefSeq gff.
    """
    nirvana_tx_set = set()

    with gzip.open(nirvana_gff) as nir_fh:

        for line in nir_fh:
            gff_gene_name = None
            gff_transcript = None
            gff_tag = ""

            fields = line.decode().strip().split("\t")
            record_type = fields[2]
            if not record_type == "transcript":
                continue

            info_field = fields[8]
            info_fields = info_field.split("; ")

            gff_transcript = None
            for field in info_fields:
                key, value = field.split(" ")

                if key == "transcript_id" and value.startswith('"NM_'):
                    gff_transcript = value.replace('"','')
                    nirvana_tx_set.add(gff_transcript)

    nirvana_tx_list = list(nirvana_tx_set)

    return nirvana_tx_list

def get_g2t_tx_list(genes2transcripts):
    """
    Extract a list of transcritps from a genes2transcripts file
    """
    g2t_tx_set = set()

    with open(genes2transcripts) as g2t_fh:
        for line in g2t_fh:
            tx = line.strip().split()[-1]
            assert(tx.startswith("NM_")), "Transcript {} not RefSeq, aborting!".format(tx)
            g2t_tx_set.add(tx)

    g2t_tx_list = list(g2t_tx_set)

    return g2t_tx_list

def check_transcripts(query_tx_list, nirvana_tx_list):
    """
    For each transcript in query list, report if present in nirvana list
    """
    missing = set()
    
    for tx in query_tx_list:
        if tx in nirvana_tx_list:
            print("\t".join([tx, "Present"]))
        else:
            print("\t".join([tx, "Absent"]))
            missing.add(tx)

    if missing:
        print("\nMissing:")
        print("\n".join(missing))
        print("\nFAILED")
    else:
        print("\nPASSED - All transcripts present")

def main(genes2transcripts, nirvana_gff):
    nirvana_tx_list = get_nirvana_tx_list(nirvana_gff)
    g2t_tx_list = get_g2t_tx_list(genes2transcripts)
    check_transcripts(g2t_tx_list, nirvana_tx_list)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])