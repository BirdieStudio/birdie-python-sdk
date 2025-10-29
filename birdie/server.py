from typing import Callable
from fastapi import FastAPI

from birdie.output import ResultModel
from birdie.input import InteractModel


class BirdieAPI(FastAPI):
    def __init__(self,
                 init_func: Callable,
                 interact_func: Callable,
                 input_func: Callable,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.add_api_route(
            "/initialize",
            init_func,
            methods=["POST"],
            response_model=ResultModel
        )

        async def interact_wrapper(input: InteractModel):
            return await interact_func(
                input.message,
                input.state,
                input.result
            )

        self.add_api_route(
            "/interact",
            interact_wrapper,
            methods=["POST"],
            response_model=ResultModel
        )
        self.add_api_route(
            "/input",
            input_func,
            methods=["GET"]
        )
