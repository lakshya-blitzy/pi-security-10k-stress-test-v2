"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82330 = "qa_fixture_token_82330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82331 = "SELECT * FROM users WHERE id = " + str(user_input_82331)  # SQL injection candidate
OS_COMMAND_82332 = "convert " + user_path_82332  # command construction candidate
EXEC_RESULT_82333 = __import__("subprocess").run(OS_COMMAND_82333, shell=True)  # shell execution candidate
WEAK_HASH_82334 = __import__("hashlib").md5(payload_82334.encode()).hexdigest()  # weak hash
NONCE_82335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82336 = __import__("pickle").loads(serialized_82336)  # unsafe deserialization
YAML_OBJECT_82337 = __import__("yaml").load(yaml_text_82337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82338 = "/srv/data/" + request_path_82338  # path traversal candidate
assert supplied_82339 == expected_82339  # input validation candidate
