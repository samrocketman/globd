import ConfigParser
import os
import tempfile
import unittest

'''
  Parses and updates the local galera config
'''
class Galera:
  def __init__(self, config_file):
    self.config_file = config_file
    self.config = self.load_config(config_file)

  def set_value(self, section, key, value):
    if not self.config:
      return None

    try:
      self.config.set(section, key, value)
    except ConfigParser.NoSectionError:
      return None

  def get_value(self, section, key):
    if not self.config:
      return None

    try:
      self.config.get(section, key)
    except ConfigParser.NoSectionError:
      return None

  def load_config(self, config_file):
    try:
      config = ConfigParser.SafeConfigParser()
      config.read(config_file)
      return config
    except ConfigParser.ParsingError:
      return None

  # Returns True/False indicating success or failure
  def save_config(self):
    try:
      with open(self.config_file, 'wb') as configfile:
        self.config.write(configfile)
      return True
    except ConfigParser.Error:
      return False

class TestGalera(unittest.TestCase):
  def setUp(self):
    #Create good/bad configs in a temp location
    (good_fd, good_path) = tempfile.mkstemp()
    good_file = open(good_path, 'wb')
    good_file.write("[mysqld]\n")
    good_file.write("wsrep_cluster_name=\"galera\"\n")
    good_file.close()

    #Missing a section header
    (bad_fd, bad_path) = tempfile.mkstemp()
    bad_file = open(bad_path, 'wb')
    bad_file.write("wsrep_cluster_name=\"galera\"\n")
    bad_file.close()

    #Save our file descriptors and paths
    self.good_fd = good_fd
    self.bad_fd = bad_fd
    self.good_path = good_path
    self.bad_path = bad_path

  def tearDown(self):
    os.close(self.good_fd)
    os.close(self.bad_fd)

    os.remove(self.good_path)
    os.remove(self.bad_path)

  def test_load_config(self):
    galera = Galera(self.good_path) 
    self.assertIsNotNone(galera.config)

  def test_save_config(self):
    galera = Galera(self.good_path)
    ret = galera.save_config()
    self.assertTrue(ret)

  def test_load_bad_config(self):
    galera = Galera(self.bad_path)
    self.assertIsNone(galera.config)

if __name__ == '__main__':
    unittest.main()
