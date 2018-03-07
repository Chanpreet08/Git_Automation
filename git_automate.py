from git import Repo
import os.path as osp
import sys

join = osp.join

class GitAutomate:
    def __init__(self):
        self.changed_file = 'new_changed_file.txt'
        self.base_dir = '/home/chanpreet/git_automation/'
        self.repo = Repo(join(self.base_dir,'git-automation'))
        self.inc_ver = 0.1
        self.changed_file_path = osp.join(self.repo.working_tree_dir,self.changed_file)
        self.origin = self.repo.remotes[0]

    def staging(self):
        self.repo.index.add([self.changed_file_path])
        self.repo.index.commit(self.commit_message)

    def get_all_tags(self):
        return self.repo.tags

    def get_latest_tag(self):
        all_tags = self.get_all_tags()
        latest_tag = str(all_tags[len(all_tags)-1])
        return float(latest_tag[1:])

    def create_new_tag(self):
        self.latest_tag = self.get_latest_tag()
        self.latest_tag = self.latest_tag + self.inc_ver
        self.latest_tag = 'v'+str(self.latest_tag)
        print self.latest_tag
        self.repo.create_tag(self.latest_tag)

    def push_tag_to_origin(self):
        self.origin.push(self.latest_tag)

    def run(self):

        try:
            self.commit_message = sys.argv[1]
        except:
            print 'No Commit Message!!'
            exit()

        self.staging()
        print 'Files committed with commit message: '+self.commit_message
        self.create_new_tag()
        print 'New Tag Created:' + self.latest_tag
        self.push_tag_to_origin()

if __name__ == '__main__':
    GitAutomate().run()




