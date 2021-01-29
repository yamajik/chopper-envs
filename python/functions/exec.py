from kess import asyncio
from typing import Optional, Dict, Any

from kess import Function
from pydantic import BaseModel


def run(scripts: str, _locals: Dict) -> Any:
    exec(scripts, globals(), _locals)
    return _locals.get("RETURN")


fn = Function()


class Options(BaseModel):
    executor: Optional[str] = None
    scripts: str


@fn.h
async def execrun(opts: Options):
    _locals = {}
    if opts.executor == "process":
        return await asyncio.run_in_process(run, opts.scripts, _locals)
    else:
        return run(opts.scripts, _locals)
