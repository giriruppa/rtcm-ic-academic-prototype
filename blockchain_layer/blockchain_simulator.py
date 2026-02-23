"""Permissioned blockchain simulator for immutable incident logging."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Block:
    index: int
    timestamp: str
    incident_hash: str
    payload: dict
    previous_hash: str
    block_hash: str


class IncidentLedger:
    def __init__(self) -> None:
        self.chain: list[Block] = [self._genesis_block()]

    def _hash_payload(self, payload: dict) -> str:
        raw = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    def _compute_block_hash(
        self, index: int, timestamp: str, incident_hash: str, previous_hash: str
    ) -> str:
        raw = f"{index}|{timestamp}|{incident_hash}|{previous_hash}".encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    def _genesis_block(self) -> Block:
        timestamp = datetime.utcnow().isoformat()
        incident_hash = self._hash_payload({"genesis": True})
        block_hash = self._compute_block_hash(0, timestamp, incident_hash, "0")
        return Block(0, timestamp, incident_hash, {"genesis": True}, "0", block_hash)

    def add_incident(self, payload: dict) -> Block:
        previous_block = self.chain[-1]
        index = len(self.chain)
        timestamp = datetime.utcnow().isoformat()
        incident_hash = self._hash_payload(payload)
        block_hash = self._compute_block_hash(index, timestamp, incident_hash, previous_block.block_hash)

        block = Block(index, timestamp, incident_hash, payload, previous_block.block_hash, block_hash)
        self.chain.append(block)
        return block

    def verify_chain(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            expected = self._compute_block_hash(
                current.index, current.timestamp, current.incident_hash, current.previous_hash
            )
            if current.previous_hash != previous.block_hash:
                return False
            if current.block_hash != expected:
                return False
        return True

    def to_dicts(self) -> list[dict]:
        return [asdict(block) for block in self.chain]
