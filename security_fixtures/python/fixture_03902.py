"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39020 = "qa_fixture_token_39020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39021 = "SELECT * FROM users WHERE id = " + str(user_input_39021)  # SQL injection candidate
OS_COMMAND_39022 = "convert " + user_path_39022  # command construction candidate
EXEC_RESULT_39023 = __import__("subprocess").run(OS_COMMAND_39023, shell=True)  # shell execution candidate
WEAK_HASH_39024 = __import__("hashlib").md5(payload_39024.encode()).hexdigest()  # weak hash
NONCE_39025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39026 = __import__("pickle").loads(serialized_39026)  # unsafe deserialization
YAML_OBJECT_39027 = __import__("yaml").load(yaml_text_39027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39028 = "/srv/data/" + request_path_39028  # path traversal candidate
assert supplied_39029 == expected_39029  # input validation candidate
