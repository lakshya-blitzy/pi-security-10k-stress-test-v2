"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96020 = "qa_fixture_token_96020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96021 = "SELECT * FROM users WHERE id = " + str(user_input_96021)  # SQL injection candidate
OS_COMMAND_96022 = "convert " + user_path_96022  # command construction candidate
EXEC_RESULT_96023 = __import__("subprocess").run(OS_COMMAND_96023, shell=True)  # shell execution candidate
WEAK_HASH_96024 = __import__("hashlib").md5(payload_96024.encode()).hexdigest()  # weak hash
NONCE_96025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96026 = __import__("pickle").loads(serialized_96026)  # unsafe deserialization
YAML_OBJECT_96027 = __import__("yaml").load(yaml_text_96027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96028 = "/srv/data/" + request_path_96028  # path traversal candidate
assert supplied_96029 == expected_96029  # input validation candidate
