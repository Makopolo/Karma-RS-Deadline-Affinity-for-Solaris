from System import *
from System.IO import *
from Deadline.Scripting import *
from Deadline.Slaves import *

def __main__(deadlinePlugin):
    job = deadlinePlugin.GetJob()
    deadlinePlugin.LogInfo("JobName: %s" % job.JobName)
    deadlinePlugin.LogInfo("JobId: %s" % job.JobId)
    gpusPerTask = deadlinePlugin.GetIntegerPluginInfoEntryWithDefault( "GPUsPerTask", 0 )
    selectGPUDevices = deadlinePlugin.GetPluginInfoEntryWithDefault( "SelectGPUDevices", "" ).strip()
    resultGPUs = []
    slaveGPUAffinity = list(deadlinePlugin.GpuAffinity())
    deadlinePlugin.LogInfo("affin gpu: %s" % slaveGPUAffinity)
    
    for i in range(15):
        if i in slaveGPUAffinity:
            path = "REDSHIFT_GPUDEVICES"
            deadlinePlugin.SetProcessEnvironmentVariable(path, str(i))
        else:
            pass
