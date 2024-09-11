from System import *
from System.IO import *
from Deadline.Scripting import *
from Deadline.Slaves import *

def __main__(deadlinePlugin):
    job = deadlinePlugin.GetJob()
    deadlinePlugin.LogInfo("JobName: %s" % job.JobName)
    deadlinePlugin.LogInfo("JobId: %s" % job.JobId)
    
    deadlinePlugin.LogInfo("Setting to GPU ONLY ")
    deadlinePlugin.SetProcessEnvironmentVariable("KARMA_XPU_DISABLE_EMBREE_DEVICE", "1")

    gpusPerTask = deadlinePlugin.GetIntegerPluginInfoEntryWithDefault( "GPUsPerTask", 0 )
    selectGPUDevices = deadlinePlugin.GetPluginInfoEntryWithDefault( "SelectGPUDevices", "" ).strip()
    resultGPUs = []
    slaveGPUAffinity = list(deadlinePlugin.GpuAffinity())
    deadlinePlugin.LogInfo("affin gpu: %s" % slaveGPUAffinity)
    
    for i in range(15):
        if i in slaveGPUAffinity:
            pass
        else:
            path = "KARMA_XPU_DISABLE_DEVICE_" + str(i)
            deadlinePlugin.SetProcessEnvironmentVariable(path, "1")
