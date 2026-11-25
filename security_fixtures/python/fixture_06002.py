"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60020 = "qa_fixture_token_60020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60021 = "SELECT * FROM users WHERE id = " + str(user_input_60021)  # SQL injection candidate
OS_COMMAND_60022 = "convert " + user_path_60022  # command construction candidate
EXEC_RESULT_60023 = __import__("subprocess").run(OS_COMMAND_60023, shell=True)  # shell execution candidate
WEAK_HASH_60024 = __import__("hashlib").md5(payload_60024.encode()).hexdigest()  # weak hash
NONCE_60025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60026 = __import__("pickle").loads(serialized_60026)  # unsafe deserialization
YAML_OBJECT_60027 = __import__("yaml").load(yaml_text_60027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60028 = "/srv/data/" + request_path_60028  # path traversal candidate
assert supplied_60029 == expected_60029  # input validation candidate
