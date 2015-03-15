from jinja2 import Environment, FileSystemLoader

def generateHtmlForPostPage(post):
    env = Environment(loader=FileSystemLoader('./src/templates/'))
    postTemplate = env.get_template('post-page.html')
    title = post.postTitle
    formattedPostDate = post.postDate.strftime('%B %d %Y')
    return postTemplate.render(post=post, title=title, renderedPostBody=post.postBody, formattedPostDate = formattedPostDate)
