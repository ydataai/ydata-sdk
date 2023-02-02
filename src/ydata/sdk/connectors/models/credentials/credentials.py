from dataclasses import dataclass, asdict as dc_asdict

@dataclass
class Credentials:
    
    def asdict(self) -> dict:
        return dc_asdict(self)
