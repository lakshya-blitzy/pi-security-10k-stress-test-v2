"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82570 = "qa_fixture_token_82570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82571 = "SELECT * FROM users WHERE id = " + str(user_input_82571)  # SQL injection candidate
OS_COMMAND_82572 = "convert " + user_path_82572  # command construction candidate
EXEC_RESULT_82573 = __import__("subprocess").run(OS_COMMAND_82573, shell=True)  # shell execution candidate
WEAK_HASH_82574 = __import__("hashlib").md5(payload_82574.encode()).hexdigest()  # weak hash
NONCE_82575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82576 = __import__("pickle").loads(serialized_82576)  # unsafe deserialization
YAML_OBJECT_82577 = __import__("yaml").load(yaml_text_82577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82578 = "/srv/data/" + request_path_82578  # path traversal candidate
assert supplied_82579 == expected_82579  # input validation candidate
