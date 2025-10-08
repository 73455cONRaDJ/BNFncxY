# 代码生成时间: 2025-10-09 03:26:24
import numpy as np

"""
Learning Effect Evaluation Program
This program evaluates the learning effect by comparing the scores of students before
and after a training session using NumPy.
"""

class LearningEffectEvaluator:
    """
    Class to evaluate the learning effect.
    """
    def __init__(self, pre_scores, post_scores):
        """
        Initializes the LearningEffectEvaluator with pre and post training scores.
        :param pre_scores: A numpy array of pre-training scores.
        :param post_scores: A numpy array of post-training scores.
        """
        self.pre_scores = np.array(pre_scores, dtype=float)
        self.post_scores = np.array(post_scores, dtype=float)

    def calculate_improvement(self):
        """
        Calculates the improvement in scores after training.
        :return: A numpy array of improvement scores.
        """
        return self.post_scores - self.pre_scores

    def calculate_average_improvement(self):
        """
        Calculates the average improvement in scores.
        :return: The average improvement score.
        """
        improvement = self.calculate_improvement()
        return np.mean(improvement)

    def calculate_median_improvement(self):
        """
        Calculates the median improvement in scores.
        :return: The median improvement score.
        """
        improvement = self.calculate_improvement()
        return np.median(improvement)

    def calculate_max_min_improvement(self):
        """
        Calculates the maximum and minimum improvement in scores.
        :return: A tuple of (max improvement, min improvement).
        """
        improvement = self.calculate_improvement()
        return np.max(improvement), np.min(improvement)

    def evaluate(self):
        """
        Evaluates the overall learning effect.
        :return: A dictionary containing average, median, max, and min improvements.
        """
        try:
            avg_improvement = self.calculate_average_improvement()
            median_improvement = self.calculate_median_improvement()
            max_improvement, min_improvement = self.calculate_max_min_improvement()
            return {
                'average_improvement': avg_improvement,
                'median_improvement': median_improvement,
                'max_improvement': max_improvement,
                'min_improvement': min_improvement
            }
        except Exception as e:
            print(f"An error occurred: {e}")
            return {}

# Example usage
if __name__ == '__main__':
    try:
        pre_scores = [50, 60, 70, 80, 90]
        post_scores = [55, 65, 75, 85, 95]
        evaluator = LearningEffectEvaluator(pre_scores, post_scores)
        evaluation_results = evaluator.evaluate()
        print(evaluation_results)
    except Exception as e:
        print(f"An error occurred: {e}")