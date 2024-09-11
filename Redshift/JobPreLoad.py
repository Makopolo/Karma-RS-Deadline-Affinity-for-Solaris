from System import *
from System.IO import *
from Deadline.Scripting import *
from Deadline.Slaves import *

def __main__(deadlinePlugin):
    job = deadlinePlugin.GetJob()
    deadlinePlugin.LogInfo("JobName: %s" % job.JobName)
    deadlinePlugin.LogInfo("JobId: %s" % job.JobId)


    
    # deadlinePlugin.LogInfo("Setting to GPU ONLY ")
    # deadlinePlugin.SetProcessEnvironmentVariable("KARMA_XPU_DISABLE_EMBREE_DEVICE", "1")
    # gpusPerTask = deadlinePlugin.GetIntegerPluginInfoEntryWithDefault( "GPUsPerTask", 0 )
    # gpusSelectDevices = deadlinePlugin.GetPluginInfoEntryWithDefault( "GPUsSelectDevices", "" )
    # slave = deadlinePlugin.GetSlaveName().lower()
    # #test = deadlinePlugin.GpuAffinity()
    # #deadlinePlugin.LogInfo(test)

    # if deadlinePlugin.OverrideGpuAffinity():
    #     deadlinePlugin.LogInfo("in overrideGPUAFFIN if")
    #     deadlinePlugin.LogInfo("gpusPerTask:  %s" % gpusPerTask)
    #     deadlinePlugin.LogInfo("gpusSelectDevices:  %s" % gpusSelectDevices)
    #     overrideGPUs = deadlinePlugin.GpuAffinity()
    #     if gpusPerTask == 0 and gpusSelectDevices != "":
    #         gpus = gpusSelectDevices.split( "," )
    #         deadlinePlugin.LogInfo("gpus: %s" % gpus)
    #         resultGPUs = []
    #         notFoundGPUs = []
    #         for gpu in gpus:
    #             if int( gpu ) in overrideGPUs:
    #                 resultGPUs.append( gpu )
    #                 deadlinePlugin.LogInfo("appen gpu: %s" % gpu)

    #             else:
    #                 #path = "KARMA_XPU_DISABLE_DEVICE_" + str(gpu)
    #                 #deadlinePlugin.LogInfo("DISABLE CERTAIN GPU ")
    #                 #deadlinePlugin.SetProcessEnvironmentVariable(path, "1")
    #                 notFoundGPUs.append( gpu )
    #                 deadlinePlugin.LogInfo("appen not found gpu: %s" % gpu)

    gpusPerTask = deadlinePlugin.GetIntegerPluginInfoEntryWithDefault( "GPUsPerTask", 0 )
    selectGPUDevices = deadlinePlugin.GetPluginInfoEntryWithDefault( "SelectGPUDevices", "" ).strip()
    resultGPUs = []
    slaveGPUAffinity = list(deadlinePlugin.GpuAffinity())
    deadlinePlugin.LogInfo("affin gpu: %s" % slaveGPUAffinity)
    
    for i in range(15):
        if i in slaveGPUAffinity:
            path = "REDSHIFT_GPUDEVICES"
            deadlinePlugin.SetProcessEnvironmentVariable(path, str(i))
            #pass
        else:
            #path = "KARMA_XPU_DISABLE_DEVICE_" + str(i)
            pass
            #deadlinePlugin.SetProcessEnvironmentVariable(path, "1")

            


    # if deadlinePlugin.OverrideGpuAffinity():
    #     slaveGPUAffinity = list(deadlinePlugin.GpuAffinity())
    #     deadlinePlugin.LogInfo("affin gpu: %s" % slaveGPUAffinity)
    #     if gpusPerTask == 0 and selectGPUDevices != "":
    #         tempGPUs = selectGPUDevices.split( "," )
    #         notFoundGPUs = []
    #         for gpu in tempGPUs:
    #             gpu = gpu.strip()
    #             if int( gpu ) in slaveGPUAffinity:
    #                 resultGPUs.append( gpu )
    #             else:
    #                 notFoundGPUs.append( gpu )
            
    #         if len( notFoundGPUs ) > 0:
    #             deadlinePlugin.LogWarning( "The Worker is overriding its GPU affinity and the following GPUs do not match the Workers affinity so they will not be used: %s" % ",".join( notFoundGPUs ) )

    #         if len( resultGPUs ) == 0:
    #             deadlinePlugin.FailRender( "The Worker does not have affinity for any of the GPUs specified in the job." )

    #     elif gpusPerTask > 0:
    #         if gpusPerTask > len( slaveGPUAffinity ):
    #             deadlinePlugin.LogWarning( "The Worker is overriding its GPU affinity and the Worker only has affinity for %s Workers of the %s requested." % ( len( slaveGPUAffinity ), gpusPerTask ) )
    #             resultGPUs = [ str( gpu ) for gpu in slaveGPUAffinity ]
    #         else:
    #             startingGPU = deadlinePlugin.GetThreadNumber() * gpusPerTask
    #             numOverrideGPUs = len( slaveGPUAffinity )
    #             startIndex = startingGPU % numOverrideGPUs
    #             endIndex = ( startingGPU + gpusPerTask) % numOverrideGPUs
    #             if startIndex < endIndex:
    #                 gpus = slaveGPUAffinity[startIndex:endIndex]
    #             else:
    #                 #If there are multiple render threads going we could roll over the available GPUs in which case we need to grab from both ends of the available GPUs
    #                 gpus = slaveGPUAffinity[ :endIndex ] + slaveGPUAffinity[ startIndex: ]
                    
    #             resultGPUs = [ str( gpu ) for gpu in gpus ]

    #     else:
    #         resultGPUs = [ str( gpu ) for gpu in slaveGPUAffinity ]
        
    #     deadlinePlugin.LogInfo( "The Worker is overriding the GPUs to render, so the following GPUs will be used: %s" % ",".join( resultGPUs ) )

    # elif gpusPerTask == 0 and selectGPUDevices != "":
    #     deadlinePlugin.LogInfo( "Specific GPUs specified, so the following GPUs will be used: %s" % selectGPUDevices )
    #     resultGPUs = selectGPUDevices.split( "," )

    # elif gpusPerTask > 0:
    #     # As of redshift 1.3 there is no command line option to specify multiple threads, but this code should still work
    #     startIndex = deadlinePlugin.GetThreadNumber() * gpusPerTask
        
    #     for i in range( startIndex, startIndex + gpusPerTask ):
    #         resultGPUs.append( str( i ) )

    #     deadlinePlugin.LogInfo( "GPUs per task is greater than 0, so the following GPUs will be used: " + ",".join( resultGPUs ) )

    # #return resultGPUs