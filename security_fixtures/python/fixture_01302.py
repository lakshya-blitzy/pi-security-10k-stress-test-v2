"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13020 = "qa_fixture_token_13020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13021 = "SELECT * FROM users WHERE id = " + str(user_input_13021)  # SQL injection candidate
OS_COMMAND_13022 = "convert " + user_path_13022  # command construction candidate
EXEC_RESULT_13023 = __import__("subprocess").run(OS_COMMAND_13023, shell=True)  # shell execution candidate
WEAK_HASH_13024 = __import__("hashlib").md5(payload_13024.encode()).hexdigest()  # weak hash
NONCE_13025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13026 = __import__("pickle").loads(serialized_13026)  # unsafe deserialization
YAML_OBJECT_13027 = __import__("yaml").load(yaml_text_13027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13028 = "/srv/data/" + request_path_13028  # path traversal candidate
assert supplied_13029 == expected_13029  # input validation candidate
