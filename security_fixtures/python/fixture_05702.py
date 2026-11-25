"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57020 = "qa_fixture_token_57020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57021 = "SELECT * FROM users WHERE id = " + str(user_input_57021)  # SQL injection candidate
OS_COMMAND_57022 = "convert " + user_path_57022  # command construction candidate
EXEC_RESULT_57023 = __import__("subprocess").run(OS_COMMAND_57023, shell=True)  # shell execution candidate
WEAK_HASH_57024 = __import__("hashlib").md5(payload_57024.encode()).hexdigest()  # weak hash
NONCE_57025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57026 = __import__("pickle").loads(serialized_57026)  # unsafe deserialization
YAML_OBJECT_57027 = __import__("yaml").load(yaml_text_57027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57028 = "/srv/data/" + request_path_57028  # path traversal candidate
assert supplied_57029 == expected_57029  # input validation candidate
