
    from functools import lru_cache
    from pathlib import Path

    from pydantic import AliasChoices, SecretStr, Field
    from pydantic_settings import BaseSettings, SettingsConfigDict

    parent = Path(__file__).parent.parent




    class Settings(BaseSettings):

        model_config = SettingsConfigDict(
            env_file=parent / ".env",
            env_file_encoding="utf-8",
            extra="ignore",
        )

        aws_access_key_id: str

        aws_secret_access_key: SecretStr = Field(
            validation_alias=AliasChoices(
                "AWS_SECRET_ACCESS_KEY",
                "AWS_SECRET_ACESS_KEY",
            )
        )

        aws_region: str = "ap-southeast-2"
        s3_bucket: str

        bedrock_chat_model: str = "amazon.nova-lite-v1:0"
        bedrock_embed_model: str = "amazon.titan-embed-text-v2:0"
        embed_dim: int = 1024

        pinecone_api_key: SecretStr
        pinecone_index_host: str
        pinecone_cloud: str = "aws"
        pinecone_region: str = "ap-southeast-2"
        pinecone_timeout: int = 180

        database_url: str
        rius_api_key: SecretStr


    @lru_cache
    def get_settings() -> Settings:
        return Settings()


    if __name__ == "__main__":
        settings = get_settings()

        print("Configuration loaded successfully!")
        print("AWS Region:", settings.aws_region)
        print("S3 Bucket:", settings.s3_bucket)
        print("Pinecone Region:", settings.pinecone_region)
