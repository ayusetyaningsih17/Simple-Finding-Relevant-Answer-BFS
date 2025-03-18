from collections import deque

def bfs_find_answer(faq_graph, start_question):
    queue = deque([start_question])
    visited = set()

    while queue:
        node = queue.popleft()
        
        if node in faq_graph.get("answers", {}):
            return faq_graph["answers"][node]

        if node not in visited:
            visited.add(node)
            neighbors = faq_graph.get(node, [])
            
            queue.extend(neighbors)

    return "No relevant answer found."

faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks are AI models inspired by the human brain.",
        "Supervised Learning": "Supervised Learning uses labeled data for training."
    }
}

question = "What is AI?"
answer = bfs_find_answer(faq_graph, question)

print(f"Question: {question}")
print(f"Answer: {answer}")