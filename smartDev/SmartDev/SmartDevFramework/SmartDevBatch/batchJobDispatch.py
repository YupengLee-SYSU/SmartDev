from SmartDevBatch import batchJobConfig
from importlib import import_module

def batchDispatcher():
    cmMap = batchJobConfig.class_method_map
    class_seq = batchJobConfig.class_seq
    if cmMap.keys() is not None:
        for tmp_class in class_seq:
            if tmp_class not in cmMap.keys():
                raise Exception("name [{0}] of class seq is not in cmMap ".format(tmp_class))
            method_list = cmMap.get(tmp_class)
            module_class = import_module(module_str)
            for tmp_method in method_list:
                print("proessing class:[{0}], method:[{1}]".format(tmp_class, tmp_method))
                obj = getattr(module_class, tmp_method)
                obj()
    return


if __name__ == "__main__":
    module_str = "SmartDevBatch.batchDemo"
    module_class = import_module(module_str)
    # module_class.Print()
    print(module_class)
    # getattr(module_class, 'Print')

    # a = batchDemo()
    # a.Print()
    b = getattr(module_class, 'Print')
    b()
    # print(b)
