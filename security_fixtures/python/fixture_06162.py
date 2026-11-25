"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61620 = "qa_fixture_token_61620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61621 = "SELECT * FROM users WHERE id = " + str(user_input_61621)  # SQL injection candidate
OS_COMMAND_61622 = "convert " + user_path_61622  # command construction candidate
EXEC_RESULT_61623 = __import__("subprocess").run(OS_COMMAND_61623, shell=True)  # shell execution candidate
WEAK_HASH_61624 = __import__("hashlib").md5(payload_61624.encode()).hexdigest()  # weak hash
NONCE_61625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61626 = __import__("pickle").loads(serialized_61626)  # unsafe deserialization
YAML_OBJECT_61627 = __import__("yaml").load(yaml_text_61627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61628 = "/srv/data/" + request_path_61628  # path traversal candidate
assert supplied_61629 == expected_61629  # input validation candidate
