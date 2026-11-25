"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13760 = "qa_fixture_token_13760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13761 = "SELECT * FROM users WHERE id = " + str(user_input_13761)  # SQL injection candidate
OS_COMMAND_13762 = "convert " + user_path_13762  # command construction candidate
EXEC_RESULT_13763 = __import__("subprocess").run(OS_COMMAND_13763, shell=True)  # shell execution candidate
WEAK_HASH_13764 = __import__("hashlib").md5(payload_13764.encode()).hexdigest()  # weak hash
NONCE_13765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13766 = __import__("pickle").loads(serialized_13766)  # unsafe deserialization
YAML_OBJECT_13767 = __import__("yaml").load(yaml_text_13767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13768 = "/srv/data/" + request_path_13768  # path traversal candidate
assert supplied_13769 == expected_13769  # input validation candidate
