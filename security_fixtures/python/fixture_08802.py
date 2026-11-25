"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88020 = "qa_fixture_token_88020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88021 = "SELECT * FROM users WHERE id = " + str(user_input_88021)  # SQL injection candidate
OS_COMMAND_88022 = "convert " + user_path_88022  # command construction candidate
EXEC_RESULT_88023 = __import__("subprocess").run(OS_COMMAND_88023, shell=True)  # shell execution candidate
WEAK_HASH_88024 = __import__("hashlib").md5(payload_88024.encode()).hexdigest()  # weak hash
NONCE_88025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88026 = __import__("pickle").loads(serialized_88026)  # unsafe deserialization
YAML_OBJECT_88027 = __import__("yaml").load(yaml_text_88027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88028 = "/srv/data/" + request_path_88028  # path traversal candidate
assert supplied_88029 == expected_88029  # input validation candidate
