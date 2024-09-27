#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import Markdown, display

# H1 스타일의 마크다운 텍스트 생성
markdown_text = "# Data Science Tools and Ecosystem"

# 마크다운 셀로 출력
display(Markdown(markdown_text))


# In[4]:


from IPython.display import Markdown, display

markdown_text = "#In this notebook, Data Science Tools and Ecosystem are summarized."

display(Markdown(markdown_text))


# In[5]:


from IPython.display import Markdown, display

# 연습 4 - 데이터 과학 언어 나열
markdown_content_4 = """
Some of the popular languages that Data Scientists use are:
1. Python
2. R
3. SQL
"""
display(Markdown(markdown_content_4))


# In[6]:


from IPython.display import Markdown, display

# 연습 5 - 데이터 과학 라이브러리 나열
markdown_content_5 = """
Some of the commonly used libraries used by Data Scientists include:
1. NumPy
2. Pandas
3. Scikit-learn
"""
display(Markdown(markdown_content_5))


# In[7]:


from IPython.display import Markdown, display

# 연습 6 - 데이터 과학 도구 표
markdown_content_6 = """
| Data Science Tools       |
|--------------------------|
| Jupyter Notebook         |
| RStudio                  |
| Apache Zeppelin          |
"""
display(Markdown(markdown_content_6))


# In[8]:


from IPython.display import Markdown, display

# 연습 7 - 산술 표현식 예제 소개
markdown_content_7 = """
### Below are a few examples of evaluating arithmetic expressions in Python.
"""
display(Markdown(markdown_content_7))


# In[15]:


# 연습 8 - 숫자를 곱하고 더하는 코드 셀
# This is a simple arithmetic expression to multiply then add integers
result = (3 * 4) + 5
result


# In[16]:


# 연습 9 - 분을 시간으로 변환하는 코드 셀

minutes = 200
hours = minutes / 60
hours


# In[13]:


from IPython.display import Markdown, display

# 연습 10 - 목표를 나열하기 위해 마크다운 셀 삽입
markdown_content_10 = """
**Objectives:**
- List popular languages for Data Science.
- List commonly used libraries for Data Science.
- Demonstrate simple arithmetic expressions in Python.
- Convert time from minutes to hours.
- Create tables to summarize information.
"""
display(Markdown(markdown_content_10))


# In[14]:


from IPython.display import Markdown, display

# 연습 11 - 작성자 이름을 나타내는 마크다운 셀 만들기
markdown_content_11 = """
## Author
Name: HYEMIN LEE
"""
display(Markdown(markdown_content_11))

