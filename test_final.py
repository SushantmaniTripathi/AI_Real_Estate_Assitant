"""Final test of hybrid agent creation"""
import sys
sys.path.insert(0, r'd:\Agents_Biz\Trading_git\ai-real-estate-assistant')

print("Testing hybrid agent creation...")

try:
    from agents.hybrid_agent import create_hybrid_agent
    from langchain_core.retrievers import BaseRetriever
    from langchain_core.documents import Document
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import BaseMessage, AIMessage
    
    # Create mock LLM
    class MockLLM(BaseChatModel):
        def _generate(self, messages, stop=None, run_manager=None, **kwargs):
            return None
        
        def invoke(self, input, config=None, **kwargs):
            return AIMessage(content="Test response")
        
        @property
        def _llm_type(self) -> str:
            return "mock"
    
    # Create mock retriever
    class MockRetriever(BaseRetriever):
        def _get_relevant_documents(self, query, *, run_manager=None):
            return [Document(page_content="Test property in Mumbai", metadata={"price": 50000, "city": "Mumbai"})]
    
    llm = MockLLM()
    retriever = MockRetriever()
    
    print("Creating hybrid agent...")
    agent = create_hybrid_agent(
        llm=llm,
        retriever=retriever,
        use_tools=True,
        verbose=False
    )
    
    print(f"✓ SUCCESS! Created agent: {type(agent).__name__}")
    print(f"  - RAG chain: {type(agent.rag_chain).__name__ if hasattr(agent, 'rag_chain') else 'N/A'}")
    print(f"  - Tool agent: {type(agent.tool_agent).__name__ if agent.tool_agent else 'None (RAG-only mode)'}")
    print("\n✓ The hybrid agent is now working!")
    
except Exception as e:
    print(f"✗ FAILED: {e}")
    import traceback
    traceback.print_exc()
