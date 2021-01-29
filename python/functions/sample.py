from kess import Function

fn = Function()

@fn.h
def sample_fn():
    return {"method": "fn"}


@fn.get("/")
def sample_get():
    return {"method": "get"}


@fn.post("/post")
def sample_post():
    return {"method": "post"}
