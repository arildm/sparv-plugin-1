import os
from sparv.api import exporter, AllSourceFilenames, AnnotationAllSourceFiles, Export


@exporter("Noun counts by document")
def nouncount_export(
    sources=AllSourceFilenames(),
    counts=AnnotationAllSourceFiles("<text>:sbx_uppercase.nouncount"),
    out=Export("sbx_uppercase/nouncounts.tsv"),
):
    for fn in sources:
        for count in counts.read(fn):
            print(f"aasf {fn} {count}")

    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write("foobar!")
