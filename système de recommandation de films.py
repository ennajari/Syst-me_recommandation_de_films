import numpy as np

class MovieRecommender:
    def __init__(self, num_users, num_movies):
        self.num_users = num_users
        self.num_movies = num_movies
        self.ratings = np.random.randint(1, 6, size=(num_users, num_movies))

    def rate_movie(self, user_id, movie_id, rating):
        self.ratings[user_id, movie_id] = rating

    def get_movie_recommendations(self, user_id, num_recommendations=5):
        user_ratings = self.ratings[user_id]
        similarity_scores = np.dot(self.ratings, user_ratings) / (np.linalg.norm(self.ratings, axis=1) * np.linalg.norm(user_ratings))
        sorted_similarities = np.argsort(similarity_scores)[::-1]

        recommendations = []
        for movie_id in range(self.num_movies):
            if user_ratings[movie_id] == 0:
                score = np.sum(similarity_scores[sorted_similarities[:10]] * self.ratings[sorted_similarities[:10], movie_id])
                recommendations.append((movie_id, score))
        
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return [movie_id for movie_id, _ in recommendations[:num_recommendations]]

def main():
    num_users = 10
    num_movies = 20
    recommender = MovieRecommender(num_users, num_movies)

    while True:
        print("\nMovie Recommender")
        print("1. Rate Movie")
        print("2. Get Recommendations")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = int(input("Enter user ID: "))
            movie_id = int(input("Enter movie ID: "))
            rating = int(input("Enter rating (1-5): "))
            recommender.rate_movie(user_id, movie_id, rating)
        elif choice == '2':
            user_id = int(input("Enter user ID: "))
            recommendations = recommender.get_movie_recommendations(user_id)
            print("\nRecommended Movies:")
            for i, movie_id in enumerate(recommendations, start=1):
                print(f"{i}. Movie {movie_id}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
