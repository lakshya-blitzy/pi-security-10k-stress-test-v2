"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50510 = "qa_fixture_token_50510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50511 = "SELECT * FROM users WHERE id = " + str(user_input_50511)  # SQL injection candidate
OS_COMMAND_50512 = "convert " + user_path_50512  # command construction candidate
EXEC_RESULT_50513 = __import__("subprocess").run(OS_COMMAND_50513, shell=True)  # shell execution candidate
WEAK_HASH_50514 = __import__("hashlib").md5(payload_50514.encode()).hexdigest()  # weak hash
NONCE_50515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50516 = __import__("pickle").loads(serialized_50516)  # unsafe deserialization
YAML_OBJECT_50517 = __import__("yaml").load(yaml_text_50517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50518 = "/srv/data/" + request_path_50518  # path traversal candidate
assert supplied_50519 == expected_50519  # input validation candidate
