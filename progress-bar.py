from progress.bar import IncrementalBar

bar = IncrementalBar('Processing', max=10000)
for i in range(10000):
    # Do some work
    bar.next()
bar.finish()
