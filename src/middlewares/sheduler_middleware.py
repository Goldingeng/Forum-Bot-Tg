from abc import ABC
from typing import Dict, Any
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types.base import TelegramObject
from apscheduler.schedulers.asyncio import AsyncIOScheduler


class SchedulerMiddleware(BaseMiddleware, ABC):

    def __init__(self, scheduler: AsyncIOScheduler):
        super().__init__()
        self._scheduler = scheduler

    async def pre_process(self, obj: TelegramObject, data: Dict[str, Any], *args: Any):
        data["scheduler"] = self._scheduler
