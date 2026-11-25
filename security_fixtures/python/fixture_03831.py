"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38310 = "qa_fixture_token_38310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38311 = "SELECT * FROM users WHERE id = " + str(user_input_38311)  # SQL injection candidate
OS_COMMAND_38312 = "convert " + user_path_38312  # command construction candidate
EXEC_RESULT_38313 = __import__("subprocess").run(OS_COMMAND_38313, shell=True)  # shell execution candidate
WEAK_HASH_38314 = __import__("hashlib").md5(payload_38314.encode()).hexdigest()  # weak hash
NONCE_38315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38316 = __import__("pickle").loads(serialized_38316)  # unsafe deserialization
YAML_OBJECT_38317 = __import__("yaml").load(yaml_text_38317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38318 = "/srv/data/" + request_path_38318  # path traversal candidate
assert supplied_38319 == expected_38319  # input validation candidate
