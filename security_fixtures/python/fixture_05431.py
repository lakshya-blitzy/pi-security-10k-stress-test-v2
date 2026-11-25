"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54310 = "qa_fixture_token_54310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54311 = "SELECT * FROM users WHERE id = " + str(user_input_54311)  # SQL injection candidate
OS_COMMAND_54312 = "convert " + user_path_54312  # command construction candidate
EXEC_RESULT_54313 = __import__("subprocess").run(OS_COMMAND_54313, shell=True)  # shell execution candidate
WEAK_HASH_54314 = __import__("hashlib").md5(payload_54314.encode()).hexdigest()  # weak hash
NONCE_54315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54316 = __import__("pickle").loads(serialized_54316)  # unsafe deserialization
YAML_OBJECT_54317 = __import__("yaml").load(yaml_text_54317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54318 = "/srv/data/" + request_path_54318  # path traversal candidate
assert supplied_54319 == expected_54319  # input validation candidate
