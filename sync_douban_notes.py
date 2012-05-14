from settings import db, douban_client, DOUBAN_UID, MAX_RESULTS

def sync_douban_notes():
    url = "http://api.douban.com/people/{0}/notes?max-results={1}".format(DOUBAN_UID, MAX_RESULTS)
    notes = douban_client.GetMyNotes(url).entry
    for note in notes:
        did = int(note.id.text.split('/')[-1])
        title = note.title.text
        published = note.published.text
        content =  note.content.text
        set_note(did, title, published, content)

def set_note(did, title, published, content):
    infos = db.mhb
    if infos.find({'did': did}).count() != 0:
        infos.update({'did': did}, {'title':title, 'published':published, 'content':content}) 
    else:
        infos.insert({'did': did, 'title':title, 'published':published, 'content':content}) 

if __name__ == "__main__":
    sync_douban_notes()
