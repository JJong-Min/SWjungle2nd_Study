class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_paragraph = []
        new_para = ''
        for para in paragraph:
            if para.isalpha():
                new_para += para.lower()
            elif new_para != '' and new_para not in banned:
                new_paragraph.append(new_para)
                new_para = ''
            else:
                new_para = ''
        if new_para:
            new_paragraph.append(new_para)
        new_para = collections.Counter(new_paragraph)
        '''
        paragraph = paragraph.split()
        new_paragraph = []
        for para in paragraph:
            new_para = ''
            for pa in para:
                if pa.isalpha():
                    new_para += pa.lower()
            if new_para not in banned:
                new_paragraph.append(new_para)
        count = collections.Counter(new_paragraph)
        '''
        return new_para.most_common(1)[0][0]
        
