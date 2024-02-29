"""
Source Code: """ """ 
Simple Documentation: This is a source code for a Python module that generates blog articles based on a given subject. It uses the dspy library and the Typer framework. The main function is the `blog_call` function, which takes in a subject and returns a markdown blog article. There is also a `blog_route` function that can be used as an API endpoint to generate blog articles.
"""
import dspy
from typer import Typer
from dspygen.utils.dspy_tools import init_dspy


app = Typer()        


class BlogModule(dspy.Module):
    """BlogModule"""

    def forward(self, subject):
        pred = dspy.Predict("subject -> markdown_blog_article")
        result = pred(subject=subject).markdown_blog_article
        return result


def blog_call(subject):
    blog = BlogModule()
    return blog.forward(subject=subject)


@app.command()
def call(subject):
    """BlogModule"""
    init_dspy()
    
    print(blog_call(subject=subject))


# TODO: Add streamlit component


from fastapi import APIRouter
router = APIRouter()

@router.post("/blog/")
async def blog_route(data: dict):
    # Your code generation logic here
    init_dspy()
    
    print(data)
    return blog_call(**data)


def main():
    init_dspy()
    subject = ""
    print(blog_call(subject=subject))
    

if __name__ == "__main__":
    main()