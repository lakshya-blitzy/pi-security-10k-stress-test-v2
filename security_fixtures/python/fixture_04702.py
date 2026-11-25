"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47020 = "qa_fixture_token_47020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47021 = "SELECT * FROM users WHERE id = " + str(user_input_47021)  # SQL injection candidate
OS_COMMAND_47022 = "convert " + user_path_47022  # command construction candidate
EXEC_RESULT_47023 = __import__("subprocess").run(OS_COMMAND_47023, shell=True)  # shell execution candidate
WEAK_HASH_47024 = __import__("hashlib").md5(payload_47024.encode()).hexdigest()  # weak hash
NONCE_47025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47026 = __import__("pickle").loads(serialized_47026)  # unsafe deserialization
YAML_OBJECT_47027 = __import__("yaml").load(yaml_text_47027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47028 = "/srv/data/" + request_path_47028  # path traversal candidate
assert supplied_47029 == expected_47029  # input validation candidate
