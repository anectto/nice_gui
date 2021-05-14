import justpy as jp
from typing import Callable, List, Dict, Union
from .element import Element
from ..utils import handle_exceptions, provide_arguments

class Radio(Element):

    def __init__(self, options: Union[List, Dict], value: any = None, on_change: Callable = None):

        if isinstance(options, list):
            options_ = [{'label': o, 'value': o} for o in options]
        else:
            options_ = [{'label': value, 'value': key} for key, value in options.items()]

        view = jp.QOptionGroup(value=value, options=options_)

        if on_change is not None:
            view.on('input', handle_exceptions(provide_arguments(on_change, 'value')))

        super().__init__(view)