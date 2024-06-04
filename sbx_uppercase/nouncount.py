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


@annotator("Number of nouns in text")
def nouncount_text(
    text: Annotation = Annotation("<text>"),
    nouncount_sent: Annotation = Annotation("<sentence>:sbx_uppercase.nouncount"),
    out: Output = Output("<text>:sbx_uppercase.nouncount"),
):
    texts, orphans = text.get_children(nouncount_sent)
    sent_nouncount_list = [int(count) for count in nouncount_sent.read()]
    n_nouns = []
    for text in texts:
        n_nouns_text = 0
        for sent_i in text:
            n_nouns_text += sent_nouncount_list[sent_i]
        n_nouns.append(str(n_nouns_text))
    out.write(n_nouns)
