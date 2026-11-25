"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84620 = "qa_fixture_token_84620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84621 = "SELECT * FROM users WHERE id = " + str(user_input_84621)  # SQL injection candidate
OS_COMMAND_84622 = "convert " + user_path_84622  # command construction candidate
EXEC_RESULT_84623 = __import__("subprocess").run(OS_COMMAND_84623, shell=True)  # shell execution candidate
WEAK_HASH_84624 = __import__("hashlib").md5(payload_84624.encode()).hexdigest()  # weak hash
NONCE_84625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84626 = __import__("pickle").loads(serialized_84626)  # unsafe deserialization
YAML_OBJECT_84627 = __import__("yaml").load(yaml_text_84627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84628 = "/srv/data/" + request_path_84628  # path traversal candidate
assert supplied_84629 == expected_84629  # input validation candidate
