from wordcloud import WordCloud


class GoogleWordCloud(object):

    STOP_WORDS = ['てる', 'いる', 'なる', 'れる', 'する', 'ある', 'こと', 'これ', 'さん', 'して',
                  'くれる', 'やる', 'くださる', 'そう', 'せる', 'した', '思う',
                  'それ', 'ここ', 'ちゃん', 'くん', '', 'て', 'に', 'を', 'は', 'の', 'が', 'と', 'た', 'し', 'で',
                  'ない', 'も', 'な', 'い', 'か', 'ので', 'よう', '']

    def __init__(self, files, font_path='fonts/NotoSansCJKjp-Regular.otf'):
        self.files = files
        self.font_path = font_path

    def out_put(self):
        for file in self.files:
            with open(file) as f:
                s = f.read()
                if len(s.split()) < 10:
                    continue
                wc = WordCloud(
                    background_color="white",
                    font_path=self.font_path,
                    stopwords=self.STOP_WORDS,
                )
                wc.generate(s)
                wc.to_file(f'{file}.png')
