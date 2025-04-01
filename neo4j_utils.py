# neo4j_utils.py

import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

class Neo4jConnection:
    def __init__(self):
        self.uri = os.getenv("NEO4J_URI")
        self.username = os.getenv("NEO4J_USERNAME")
        self.password = os.getenv("NEO4J_PASSWORD")
        self.driver = GraphDatabase.driver(self.uri, auth=(self.username, self.password))

    def close(self):
        if self.driver is not None:
            self.driver.close()

    def test_connection(self):
        with self.driver.session() as session:
            result = session.run("RETURN 'Neo4j connection successful!' AS message")
            return result.single()["message"]

    def add_chunk_as_node(self, chunk_text: str, index: int):
        with self.driver.session() as session:
            session.run("""
                CREATE (c:Chunk {id: $id, content: $content})
            """, id=index, content=chunk_text)

    def create_relationship(self, source_id: int, target_id: int):
        with self.driver.session() as session:
            session.run("""
                MATCH (a:Chunk {id: $source_id}), (b:Chunk {id: $target_id})
                MERGE (a)-[:NEXT]->(b)
            """, source_id=source_id, target_id=target_id)

    def store_chunks(self, chunks):
        with self.driver.session() as session:
            for i, chunk in enumerate(chunks):
                session.run(
                    "CREATE (c:Chunk {id: $id, content: $content})",
                    id=i,
                    content=chunk
                )
                if i > 0:
                    self.create_relationship(i - 1, i)

    def get_all_chunks(self):
        with self.driver.session() as session:
            result = session.run("MATCH (c:Chunk) RETURN c.content AS content")
            return [record["content"] for record in result]

    def clear_all_chunks(self):
        with self.driver.session() as session:
            session.run("MATCH (c:Chunk) DETACH DELETE c")
