from ipaddress import IPv4Address


k8s_cluster = []


class NodeIPAddressAleradyUsed(Exception):
    pass
    
    
class NodeAlreadyJoin(Exception):
    pass


class Node:
    def __init__(self, ip_address) -> None:
        self.ip_address = IPv4Address(ip_address)
        self.__is_join = False

    def join(self, k8s_cluster) -> None:
        try:
            if (self.__is_join == True):
                raise NodeAlreadyJoin()
            else: 
                self.__is_join = True
                k8s_cluster.append(self)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise
        
        
class ControlPlane(Node):
    pass


class Worker(Node):
    pass


if __name__ == '__main__':
    master1 = ControlPlane("192.168.0.1")
    master2 = ControlPlane("192.168.0.2")
    worker1 = Worker("192.168.1.1")
    worker2 = Worker("192.168.1.2")
    master1.join(k8s_cluster)
    worker1.join(k8s_cluster)
    worker2.join(k8s_cluster)
    worker2.join(k8s_cluster)
    print(k8s_cluster)
