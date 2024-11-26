from resources.connections import JWT_SECRET


def hello():
    version = "2.0"
    if JWT_SECRET:
        return f"NoHarm - GetName {version} (AUTH)\n\nServiço de nomes habilitado! Volte para a NoHarm e use o sistema normalmente ;)\n\n"

    return f"NoHarm - GetName {version}\n\nServiço de nomes habilitado! Volte para a NoHarm e use o sistema normalmente ;)\n\n"
