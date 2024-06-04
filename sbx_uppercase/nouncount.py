from sparv.api import annotator, Annotation, Output


@annotator("Number of nouns in sentence")
def nouncount(
    sent: Annotation = Annotation("<sentence>"),
    pos: Annotation = Annotation("<token:pos>"),
    out: Output = Output("<sentence>:sbx_uppercase.nouncount"),
):
    sents, orphans = sent.get_children(pos)
    pos_list = list(pos.read())
    n_nouns = []
    for sent in sents:
        n_nouns_sent = 0
        for i in sent:
            if pos_list[i] == "NN":
                n_nouns_sent += 1
        n_nouns.append(str(n_nouns_sent))
    out.write(n_nouns)
