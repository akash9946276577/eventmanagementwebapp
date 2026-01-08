from django import template

register=template.Library()

@register.filter(name='decchunks')
def decchunks(declist_data,decchunk_size):
    decchunk=[]
    i=0
    for data in declist_data:
        decchunk.append(data)
        i=i+1
        if i == decchunk_size:
            yield decchunk
            i=0
            decchunk=[]
    yield decchunk
