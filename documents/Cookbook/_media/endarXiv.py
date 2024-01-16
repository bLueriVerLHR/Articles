### [demo]
import pybtex.database as btexdb

citation = """
@misc{dao2022flashattention,
      title={FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness}, 
      author={Tri Dao and Daniel Y. Fu and Stefano Ermon and Atri Rudra and Christopher Ré},
      year={2022},
      eprint={2205.14135},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
"""

bibtex = btexdb.parse_string(citation, "bibtex")

for entry in bibtex.entries.values():
    print("%0 Journal Article")
    print("%T {}".format(entry.fields['title']))
    for p in entry.persons['author']:
        print("%A {}".format(p))
    print("%J arXiv preprint arXiv:{}".format(entry.fields['eprint']))
    print("%D {}".format(entry.fields['year']))
### [demo]
