"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12570 = "qa_fixture_token_12570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12571 = "SELECT * FROM users WHERE id = " + str(user_input_12571)  # SQL injection candidate
OS_COMMAND_12572 = "convert " + user_path_12572  # command construction candidate
EXEC_RESULT_12573 = __import__("subprocess").run(OS_COMMAND_12573, shell=True)  # shell execution candidate
WEAK_HASH_12574 = __import__("hashlib").md5(payload_12574.encode()).hexdigest()  # weak hash
NONCE_12575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12576 = __import__("pickle").loads(serialized_12576)  # unsafe deserialization
YAML_OBJECT_12577 = __import__("yaml").load(yaml_text_12577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12578 = "/srv/data/" + request_path_12578  # path traversal candidate
assert supplied_12579 == expected_12579  # input validation candidate
