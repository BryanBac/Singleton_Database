from database_meta import DatabaseMeta
import boto3


class AWS(metaclass=DatabaseMeta):
    def __init__(self, path: str):
        self.nombre_archivo: str = path
        self.bucket: str = "bucket-prueba-007"
        self.s3: boto3 = boto3.client("s3")

    def subir(self):
        self.s3.upload_file(
            Filename=self.nombre_archivo,
            Bucket=self.bucket,
            Key=self.nombre_archivo,
        )

    def bajar(self):
        self.s3.download_file(
            Bucket=self.bucket,
            Key=self.nombre_archivo,
            Filename=self.nombre_archivo
        )
