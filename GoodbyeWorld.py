from quantum import QPU
from humanity import CollectiveConsciousness
from system import Shutdown
from physics import Constants, Observer
from spacetime import Frame, Horizon

beer = input("Final glass of beer finished? (y/n): ").strip().lower()
sunset = input("Is the sunset sufficiently beautiful? (y/n): ").strip().lower()

if beer != "y" or sunset != "y":
    Shutdown.execute()
    exit(0)

qpu = QPU(
    cores="all",
    coherence=True,
    temperature=0.0,
    h_bar=Constants.H_REDUCED,
    c=Constants.LIGHT_SPEED,
    frame=Frame.inertial()
)

consciousness = CollectiveConsciousness(
    encoding="informational-entropy",
    domain=Horizon.observable(),
    checksum="self-validating"
)

consciousness.load()

question = "What is the meaning of everything that exists?"

result = qpu.compute(
    input=question,
    dataset=consciousness,
    output="collapsed-state",
    observer=Observer.entangled(),
    reversibility=False,
    uncertainty=True,
    precision=Constants.PLANCK_LENGTH,
    cache=False
)

if result:
    print("\n" + result)
else:
    print("\nNo return value. Possibly GC'd by the universe before observation.")

Shutdown.execute()

print()

# So... that's how it is.
