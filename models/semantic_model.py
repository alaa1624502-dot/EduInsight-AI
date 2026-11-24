from sentence_transformers import SentenceTransformer, util

class EduInsightModel:

def __init__(self):
    self.model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

def compare_answers(self, student_answer, correct_answer):

    student_embedding = self.model.encode(
        student_answer,
        convert_to_tensor=True
    )

    correct_embedding = self.model.encode(
        correct_answer,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        student_embedding,
        correct_embedding
    ).item()

    return round(similarity * 100, 2)
if name == "main":

ai = EduInsightModel()

correct = "Photosynthesis is the process by which plants make food using sunlight."

student = "Plants use sunlight to produce their own food."

score = ai.compare_answers(student, correct)

print("Semantic Similarity:", score, "%")
