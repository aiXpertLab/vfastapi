from fastapi import APIRouter
from httpx import request
from app.schemas.sch_query import QueryString
from app.component.langchain_agent import executor
from langchain_core.messages import HumanMessage, AIMessage

import logging
logger = logging.getLogger(__name__)

agentRou = APIRouter()


@agentRou.post("/wage-agent")
def wage_dispatch(request: QueryString, debug: bool = False):
    logger.info("User query: %s", request.query)

    result = executor.invoke(
        {"messages": [HumanMessage(content=request.query)]}
    )

    answer_text = result["output"]

    route = "LLM"
    # Detect tool calls
    for msg in result.get("messages", []):
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            route = msg.tool_calls[0].name
            break

    response = {
        "query": request.query,
        "route": route,
        "answer": answer_text,
    }
    if debug:
        response["messages"] = result["messages"]

    return response
