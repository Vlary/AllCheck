import zstandard
import io


with open('linux.zck', 'rb') as f:
    dctx = zstandard.ZstdDecompressor()
    stream_reader = dctx.stream_reader(f)
    text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
    for line in text_stream:
        print(line.strip())
    f.close()
