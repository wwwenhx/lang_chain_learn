from langchain_community.tools.tavily_search import TavilySearchResults
import threading

_tavily_search=None

_lock = threading.Lock()  # 保证多线程安全

def search_load():
    global _tavily_search
    if _tavily_search is None:
        with _lock:
            if _tavily_search is None:
                _tavily_search=TavilySearchResults()
    return _tavily_search