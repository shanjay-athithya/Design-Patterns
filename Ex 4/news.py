from BinaryTree.BinarySearchTree import BinarySearchTree

class News:
    def __init__(self):
        self.political = BinarySearchTree()
        self.sports = BinarySearchTree()
    
    def construct_news_tree(self, type, data):
        if type == 'political':
            self.political.construct(data)
        elif type == 'sports':
            self.sports.construct(data)
    
    def add_news(self, type, date, news):
        data = f"{date}:{news}"
        if type == 'political':
            self.political.insert(data, self.political.root)
        elif type == 'sports':
            self.sports.insert(data, self.sports.root)
    
    def display_news(self, type, date):
        if type == 'political':
            political_news = self.political._inorder(self.political.root)
            for news in political_news:
                if news.startswith(date):
                    print(news)
        elif type == 'sports':
            sports_news = self.sports._inorder(self.sports.root)
            for news in sports_news:
                if news.startswith(date):
                    print(news)
                    
if __name__ == '__main__':
    news_manager = News()

    # Construct news trees
    news_manager.construct_news_tree('political', ["2023-09-30: Political news 1", "2023-09-30: Political news 2"])
    news_manager.construct_news_tree('sports', ["2023-09-30: Sports news 1", "2023-09-29: Sports news 2"])

    # Add news articles
    news_manager.add_news('political', "2023-09-30", "New Political Article")
    news_manager.add_news('sports', "2023-09-29", "New Sports Article")

    # Display news by date
    print("Political News on 2023-09-30:")
    news_manager.display_news('political', "2023-09-30")

    print("\nSports News on 2023-09-29:")
    news_manager.display_news('sports', "2023-09-29")
               