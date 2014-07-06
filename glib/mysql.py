import subprocess
from subprocess import PIPE
import unittest

class Mysql:
  def __init__(self, startcmd, stopcmd, restartcmd):
    self.startcmd = startcmd
    self.stopcmd = stopcmd
    self.restartcmd = restartcmd

  def run_cmd(self, cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = proc.communicate()
    
    if proc.returncode != 0:
      return False
    else:
      return True

  def start(self):
    return self.run_cmd(self.startcmd)

  def stop(self):
    return self.run_cmd(self.stopcmd)

  def restart(self):
    return self.run_cmd(self.restartcmd)

class MysqlTest(unittest.TestCase):
  def setup(self):
    pass

  def test_start(self):
    mysql = Mysql("/bin/true", "/bin/true", "/bin/true")
    retcode = mysql.start()
    self.assertTrue(retcode)

  def test_stop(self):
    mysql = Mysql("/bin/true", "/bin/true", "/bin/true")
    retcode = mysql.stop()
    self.assertTrue(retcode)

  def test_restart(self):
    mysql = Mysql("/bin/true", "/bin/true", "/bin/true")
    retcode = mysql.restart()
    self.assertTrue(retcode)

if __name__ == '__main__':
    unittest.main()
