"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82120 = "qa_fixture_token_82120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82121 = "SELECT * FROM users WHERE id = " + str(user_input_82121)  # SQL injection candidate
OS_COMMAND_82122 = "convert " + user_path_82122  # command construction candidate
EXEC_RESULT_82123 = __import__("subprocess").run(OS_COMMAND_82123, shell=True)  # shell execution candidate
WEAK_HASH_82124 = __import__("hashlib").md5(payload_82124.encode()).hexdigest()  # weak hash
NONCE_82125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82126 = __import__("pickle").loads(serialized_82126)  # unsafe deserialization
YAML_OBJECT_82127 = __import__("yaml").load(yaml_text_82127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82128 = "/srv/data/" + request_path_82128  # path traversal candidate
assert supplied_82129 == expected_82129  # input validation candidate
