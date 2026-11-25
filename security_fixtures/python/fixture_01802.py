"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18020 = "qa_fixture_token_18020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18021 = "SELECT * FROM users WHERE id = " + str(user_input_18021)  # SQL injection candidate
OS_COMMAND_18022 = "convert " + user_path_18022  # command construction candidate
EXEC_RESULT_18023 = __import__("subprocess").run(OS_COMMAND_18023, shell=True)  # shell execution candidate
WEAK_HASH_18024 = __import__("hashlib").md5(payload_18024.encode()).hexdigest()  # weak hash
NONCE_18025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18026 = __import__("pickle").loads(serialized_18026)  # unsafe deserialization
YAML_OBJECT_18027 = __import__("yaml").load(yaml_text_18027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18028 = "/srv/data/" + request_path_18028  # path traversal candidate
assert supplied_18029 == expected_18029  # input validation candidate
