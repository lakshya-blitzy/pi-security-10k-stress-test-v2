"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44020 = "qa_fixture_token_44020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44021 = "SELECT * FROM users WHERE id = " + str(user_input_44021)  # SQL injection candidate
OS_COMMAND_44022 = "convert " + user_path_44022  # command construction candidate
EXEC_RESULT_44023 = __import__("subprocess").run(OS_COMMAND_44023, shell=True)  # shell execution candidate
WEAK_HASH_44024 = __import__("hashlib").md5(payload_44024.encode()).hexdigest()  # weak hash
NONCE_44025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44026 = __import__("pickle").loads(serialized_44026)  # unsafe deserialization
YAML_OBJECT_44027 = __import__("yaml").load(yaml_text_44027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44028 = "/srv/data/" + request_path_44028  # path traversal candidate
assert supplied_44029 == expected_44029  # input validation candidate
