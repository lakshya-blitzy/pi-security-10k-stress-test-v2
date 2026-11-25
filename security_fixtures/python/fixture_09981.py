"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99810 = "qa_fixture_token_99810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99811 = "SELECT * FROM users WHERE id = " + str(user_input_99811)  # SQL injection candidate
OS_COMMAND_99812 = "convert " + user_path_99812  # command construction candidate
EXEC_RESULT_99813 = __import__("subprocess").run(OS_COMMAND_99813, shell=True)  # shell execution candidate
WEAK_HASH_99814 = __import__("hashlib").md5(payload_99814.encode()).hexdigest()  # weak hash
NONCE_99815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99816 = __import__("pickle").loads(serialized_99816)  # unsafe deserialization
YAML_OBJECT_99817 = __import__("yaml").load(yaml_text_99817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99818 = "/srv/data/" + request_path_99818  # path traversal candidate
assert supplied_99819 == expected_99819  # input validation candidate
