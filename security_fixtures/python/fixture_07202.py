"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72020 = "qa_fixture_token_72020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72021 = "SELECT * FROM users WHERE id = " + str(user_input_72021)  # SQL injection candidate
OS_COMMAND_72022 = "convert " + user_path_72022  # command construction candidate
EXEC_RESULT_72023 = __import__("subprocess").run(OS_COMMAND_72023, shell=True)  # shell execution candidate
WEAK_HASH_72024 = __import__("hashlib").md5(payload_72024.encode()).hexdigest()  # weak hash
NONCE_72025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72026 = __import__("pickle").loads(serialized_72026)  # unsafe deserialization
YAML_OBJECT_72027 = __import__("yaml").load(yaml_text_72027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72028 = "/srv/data/" + request_path_72028  # path traversal candidate
assert supplied_72029 == expected_72029  # input validation candidate
