import pyshorteners

def shorter_url(s:str):
    #initialise the shortner

    pys = pyshorteners.Shortener()

    #using the tiny url to shorten 
    short_url = pys.tinyurl.short(s)

    return 'short url is ', short_url

print(shorter_url("https://www.google.com/search?q=python+documentation&newwindow=1&sxsrf=ALiCzsYze-G2AArMZtCrJfyfVcqq6z8Rwg%3A1662044120968&ei=2McQY4PaOp68xc8Pyp-qIA&oq=python+do&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6DQguEMcBENEDELADEEM6BwgAELADEEM6BAgjECc6BAgAEEM6BAguECdKBAhBGABKBAhGGABQ1xBY70JgxlVoAXABeACAAYgBiAGWCJIBAzAuOZgBAKABAcgBCsABAQ&sclient=gws-wiz"))