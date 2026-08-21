from app.db import crud, GetDB
from app.models.node import NodeStatus


class MarzNodeDB:
    def list_users(self):
        with GetDB() as db:
            relations = crud.get_node_users(db, self.id)
            users = dict()
            for rel in relations:
                if not users.get(rel[0]):
                    users[rel[0]] = dict(
                        username=rel[1], id=rel[0], key=rel[2], inbounds=[]
                    )
                users[rel[0]]["inbounds"].append(rel[3].tag)
        return list(users.values())

    def store_backends(self, backends):
        inbounds = [
            inbound for backend in backends for inbound in backend.inbounds
        ]
        with GetDB() as db:
            crud.ensure_node_backends(db, backends, self.id)
            crud.ensure_node_inbounds(db, inbounds, self.id)
            # nodes.xray_version has a column and an API field but nothing ever
            # wrote to it, so every node reported a null core version - which is
            # exactly the thing you want to read before touching a node.
            version = next(
                (b.version for b in backends if b.type == "xray" and b.version),
                None,
            )
            if version:
                crud.update_node_version(db, self.id, version)

    def set_status(self, status: NodeStatus, message: str | None = None):
        with GetDB() as db:
            crud.update_node_status(db, self.id, status, message)
