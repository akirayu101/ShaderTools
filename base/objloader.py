__author__ = 'akirayu101'


def load_obj(filename):
    num = 0
    verts = []
    norms = []
    verts_out = []
    norms_out = []

    with open(filename) as f:
        for line in f:
            vals = line.split()
            if vals[0] == 'v':
                v = tuple(map(float, vals[1:4]))
                verts.append(v)
            elif vals[0] == 'vn':
                n = tuple(map(float, vals[1:4]))
                norms.append(n)
            elif vals[0] == 'f':
                for s in vals[1:]:
                    vn = s.split("/")
                # OBJ Files are 1-indexed so we must subtract 1 below
                    verts_out.append(list(verts[int(vn[0]) - 1]))
                    norms_out.append(list(norms[int(vn[2]) - 1]))
                    num += 1

    return verts_out, norms_out
