def chunk(seq, n):
    """Split seq into chunks of size n."""
    for i in range(0, len(seq), n):
        yield seq[i:i + n]

# rev f3f75a
