import subprocess
from subprocess import PIPE
import unittest

class Mysql:
  def __init__(self, startcmd, stopcmd, restartcmd, statuscmd):
    self.startcmd = startcmd
    self.stopcmd = stopcmd
    self.restartcmd = restartcmd
    self.statuscmd = statuscmd

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

  def status(self):
    return self.run_cmd(self.statuscmd)

class MysqlTest(unittest.TestCase):
  def setup(self):
    pass

  def test_start(self):
    mysql = Mysql("/bin/true", "/bin/true", "/bin/true", "/bin/true")
    retcode = mysql.start()
    self.assertTrue(retcode)

  def test_stop(self):
    mysql = Mysql("/bin/true", "/bin/true", "/bin/true", "/bin/true")
    retcode = mysql.stop()
    self.assertTrue(retcode)

  def test_restart(self):
    mysql = Mysql("/bin/true", "/bin/true", "/bin/true", "/bin/true")
    retcode = mysql.restart()
    self.assertTrue(retcode)

  def test_status(self):
    mysql = Mysql("/bin/true", "/bin/true", "/bin/true", "/bin/true")
    retcode = mysql.status()
    self.assertTrue(retcode)

  def test_bad_start(self):
    mysql = Mysql("/bin/false", "/bin/false", "/bin/false", "/bin/false")
    retcode = mysql.start()
    self.assertFalse(retcode)

  def test_bad_stop(self):
    mysql = Mysql("/bin/false", "/bin/false", "/bin/false", "/bin/false")
    retcode = mysql.stop()
    self.assertFalse(retcode)

  def test_bad_restart(self):
    mysql = Mysql("/bin/false", "/bin/false", "/bin/false", "/bin/false")
    retcode = mysql.restart()
    self.assertFalse(retcode)

  def test_bad_status(self):
    mysql = Mysql("/bin/false", "/bin/false", "/bin/false", "/bin/false")
    retcode = mysql.status()
    self.assertFalse(retcode)

if __name__ == '__main__':
    unittest.main()
