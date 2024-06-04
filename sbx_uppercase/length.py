from sparv.api import annotator, Annotation, Output

@annotator("Word length")
def length(
    word: Annotation = Annotation("<token:word>"),
    out: Output = Output("<token>:sbx_uppercase.length")
):
    out.write([str(len(word)) for word in word.read()])