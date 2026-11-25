"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6020 = "qa_fixture_token_6020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6021 = "SELECT * FROM users WHERE id = " + str(user_input_6021)  # SQL injection candidate
OS_COMMAND_6022 = "convert " + user_path_6022  # command construction candidate
EXEC_RESULT_6023 = __import__("subprocess").run(OS_COMMAND_6023, shell=True)  # shell execution candidate
WEAK_HASH_6024 = __import__("hashlib").md5(payload_6024.encode()).hexdigest()  # weak hash
NONCE_6025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6026 = __import__("pickle").loads(serialized_6026)  # unsafe deserialization
YAML_OBJECT_6027 = __import__("yaml").load(yaml_text_6027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6028 = "/srv/data/" + request_path_6028  # path traversal candidate
assert supplied_6029 == expected_6029  # input validation candidate
