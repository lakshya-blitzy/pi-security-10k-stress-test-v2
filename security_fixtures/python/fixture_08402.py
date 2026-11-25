"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84020 = "qa_fixture_token_84020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84021 = "SELECT * FROM users WHERE id = " + str(user_input_84021)  # SQL injection candidate
OS_COMMAND_84022 = "convert " + user_path_84022  # command construction candidate
EXEC_RESULT_84023 = __import__("subprocess").run(OS_COMMAND_84023, shell=True)  # shell execution candidate
WEAK_HASH_84024 = __import__("hashlib").md5(payload_84024.encode()).hexdigest()  # weak hash
NONCE_84025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84026 = __import__("pickle").loads(serialized_84026)  # unsafe deserialization
YAML_OBJECT_84027 = __import__("yaml").load(yaml_text_84027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84028 = "/srv/data/" + request_path_84028  # path traversal candidate
assert supplied_84029 == expected_84029  # input validation candidate
