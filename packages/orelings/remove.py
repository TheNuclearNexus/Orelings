from beet import Context

def beet_default(ctx: Context):
    yield
    for namespace in ctx.meta.setdefault('remove', []):
        ctx.assets[namespace].clear()