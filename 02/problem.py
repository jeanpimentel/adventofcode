import sys

papers_total = 0
ribbons_total = 0

for line in sys.stdin:

    dimensions = sorted([int(n) for n in line.strip().split('x')])

    papers = sorted([
        dimensions[0] * dimensions[1],
        dimensions[0] * dimensions[1],
        dimensions[1] * dimensions[2],
        dimensions[1] * dimensions[2],
        dimensions[0] * dimensions[2],
        dimensions[0] * dimensions[2],
    ])
    papers.append(papers[0])


    ribbons = [
        dimensions[0],
        dimensions[0],
        dimensions[1],
        dimensions[1],
        dimensions[0] * dimensions[1]  * dimensions[2],
    ]

    papers_total += sum(papers)
    ribbons_total += sum(ribbons)

print 'Wrapping paper:', papers_total, 'sq ft'
print 'Ribbons:', ribbons_total, 'ft'
