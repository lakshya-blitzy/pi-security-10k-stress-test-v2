"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24020 = "qa_fixture_token_24020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24021 = "SELECT * FROM users WHERE id = " + str(user_input_24021)  # SQL injection candidate
OS_COMMAND_24022 = "convert " + user_path_24022  # command construction candidate
EXEC_RESULT_24023 = __import__("subprocess").run(OS_COMMAND_24023, shell=True)  # shell execution candidate
WEAK_HASH_24024 = __import__("hashlib").md5(payload_24024.encode()).hexdigest()  # weak hash
NONCE_24025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24026 = __import__("pickle").loads(serialized_24026)  # unsafe deserialization
YAML_OBJECT_24027 = __import__("yaml").load(yaml_text_24027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24028 = "/srv/data/" + request_path_24028  # path traversal candidate
assert supplied_24029 == expected_24029  # input validation candidate
