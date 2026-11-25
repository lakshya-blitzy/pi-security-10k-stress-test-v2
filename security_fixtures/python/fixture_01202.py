"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12020 = "qa_fixture_token_12020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12021 = "SELECT * FROM users WHERE id = " + str(user_input_12021)  # SQL injection candidate
OS_COMMAND_12022 = "convert " + user_path_12022  # command construction candidate
EXEC_RESULT_12023 = __import__("subprocess").run(OS_COMMAND_12023, shell=True)  # shell execution candidate
WEAK_HASH_12024 = __import__("hashlib").md5(payload_12024.encode()).hexdigest()  # weak hash
NONCE_12025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12026 = __import__("pickle").loads(serialized_12026)  # unsafe deserialization
YAML_OBJECT_12027 = __import__("yaml").load(yaml_text_12027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12028 = "/srv/data/" + request_path_12028  # path traversal candidate
assert supplied_12029 == expected_12029  # input validation candidate
