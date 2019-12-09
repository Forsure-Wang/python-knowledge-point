#/usr/bin/python
import os
def get_file_list(file_path):
  dir_list = os.listdir(file_path)
  if not dir_list:
    return
  else:
    print "the raw directory list:\n {0} \n".format(dir_list)
    postgres_dir_list = list(filter(lambda x: "postgres" in x, dir_list))
    print "filtered by specify string:\n {0} \n".format(postgres_dir_list)

    # os.path.getmtime()
    # os.path.getctime()
    sorted_dir_list = sorted(postgres_dir_list, key=lambda x: os.path.getctime(os.path.join(file_path, x)), reverse=True)
    print "sorted by modified time of the files:\n {0} \n".format(sorted_dir_list)
    print sorted_dir_list[0]

if __name__ == "__main__":

    get_file_list('/home/w15021/')
    
# Get the newest file with given filter in specified directory
