"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41020 = "qa_fixture_token_41020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41021 = "SELECT * FROM users WHERE id = " + str(user_input_41021)  # SQL injection candidate
OS_COMMAND_41022 = "convert " + user_path_41022  # command construction candidate
EXEC_RESULT_41023 = __import__("subprocess").run(OS_COMMAND_41023, shell=True)  # shell execution candidate
WEAK_HASH_41024 = __import__("hashlib").md5(payload_41024.encode()).hexdigest()  # weak hash
NONCE_41025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41026 = __import__("pickle").loads(serialized_41026)  # unsafe deserialization
YAML_OBJECT_41027 = __import__("yaml").load(yaml_text_41027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41028 = "/srv/data/" + request_path_41028  # path traversal candidate
assert supplied_41029 == expected_41029  # input validation candidate
