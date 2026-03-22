"""Test if the Pydantic fix works"""
import sys
sys.path.insert(0, r'd:\Agents_Biz\Trading_git\ai-real-estate-assistant')

try:
    from vector_store.chroma_store import ChromaPropertyStore
    from vector_store.hybrid_retriever import AdvancedPropertyRetriever, create_retriever
    
    print("✓ Imports successful")
    
    # Try to create a mock retriever to test validation
    class MockStore:
        def __init__(self):
            self.collection = 'properties'
        
        def get_retriever(self, **kwargs):
            return self
        
        def get_relevant_documents(self, query):
            return []
        
        def search(self, query, k=5, filter=None):
            return []
    
    mock_store = MockStore()
    
    # Test creating retriever with geo filters (which creates AdvancedPropertyRetriever)
    retriever = create_retriever(
        vector_store=mock_store,
        k=5,
        center_lat=19.0760,
        center_lon=72.8777,
        radius_km=10.0
    )
    
    print(f"✓ Created retriever: {type(retriever).__name__}")
    print("✓ All tests passed! The fix should work.")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
