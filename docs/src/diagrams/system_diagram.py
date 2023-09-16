from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

with Diagram("System Diagram", filename="system_diagram", outformat="svg", show=False):

    user = Person(name="User", description="User is a person who uses Ligne.")

    with SystemBoundary("Frontend"):
        unity_frontend = System(name="UnityFrontend")
        # network_frontend = System(name="NetworkFrontend")
    

    with SystemBoundary("Core"):    
        ligne_core_api = System(name="LigneCoreAPI", description="LigneCore is a backend system that provides the core functionality of Ligne.")
        ligne_core_state_store = System(name="LigneCoreStateStore", description="LigneCoreStateStore is a database that stores the state of LigneCore.")

    in_memory_state = Database(name="InMemoryState", description="InMemoryState is a database that stores the state of LigneCore in-memory.")
    snapshot = Database(name="Snapshot", description="Snapshot is a database that stores the snapshots of the LigneCoreStateStore.")

    user >> Relationship("Uses") >> unity_frontend
    unity_frontend >>  Relationship("Uses") >> ligne_core_api
    # network_frontend >>  Relationship("Uses") >> ligne_core_api
    ligne_core_api >> Relationship("Uses") >> ligne_core_state_store
    ligne_core_state_store >> Relationship("Uses") >> snapshot
    ligne_core_state_store >> Relationship("Uses") >> in_memory_state