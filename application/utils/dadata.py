import json
import logging
from typing import List

import aiohttp
from pydantic import BaseModel

from application.settings import get_settings


dadata_params = get_settings().dadata_params
logger = logging.getLogger(__name__)


class Data(BaseModel):
    code: str
    alfa2: str
    alfa3: str
    name_short: str
    name: str


class Suggestion(BaseModel):
    value: str
    unrestricted_value: str
    data: Data


class Response(BaseModel):
    suggestions: List[Suggestion]


async def get_country_code(country: str) -> str:
    async with aiohttp.ClientSession(
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'Token {dadata_params.token}',
            }
    ) as session:
        async with session.post(
                dadata_params.url, data=json.dumps({"query": country})
        ) as resp:
            country_code = ''
            try:
                response = Response(**await resp.json())
                if len(response.suggestions) == 1:
                    country_code = response.suggestions[0].data.code
            except Exception as exc:
                logger.error(exc)
            return country_code
