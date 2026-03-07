from .heartbeat import router as HeartbeatRouter
from .registry import RouterConfig

all_routers: list[RouterConfig] = [
    RouterConfig(router=HeartbeatRouter, prefix="/heartbeat", tags=["Heartbeat"])
]
