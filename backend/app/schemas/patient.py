from pydantic import BaseModel, ConfigDict


class PatientBase(BaseModel):
    name: str
    gender: str = "Nam"
    birthday: str | None = None
    phone: str
    address: str | None = None


class PatientCreate(PatientBase):
    pass


class PatientUpdate(BaseModel):
    name: str | None = None
    gender: str | None = None
    birthday: str | None = None
    phone: str | None = None
    address: str | None = None


class PatientOut(PatientBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
