"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71020 = "qa_fixture_token_71020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71021 = "SELECT * FROM users WHERE id = " + str(user_input_71021)  # SQL injection candidate
OS_COMMAND_71022 = "convert " + user_path_71022  # command construction candidate
EXEC_RESULT_71023 = __import__("subprocess").run(OS_COMMAND_71023, shell=True)  # shell execution candidate
WEAK_HASH_71024 = __import__("hashlib").md5(payload_71024.encode()).hexdigest()  # weak hash
NONCE_71025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71026 = __import__("pickle").loads(serialized_71026)  # unsafe deserialization
YAML_OBJECT_71027 = __import__("yaml").load(yaml_text_71027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71028 = "/srv/data/" + request_path_71028  # path traversal candidate
assert supplied_71029 == expected_71029  # input validation candidate
