"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24620 = "qa_fixture_token_24620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24621 = "SELECT * FROM users WHERE id = " + str(user_input_24621)  # SQL injection candidate
OS_COMMAND_24622 = "convert " + user_path_24622  # command construction candidate
EXEC_RESULT_24623 = __import__("subprocess").run(OS_COMMAND_24623, shell=True)  # shell execution candidate
WEAK_HASH_24624 = __import__("hashlib").md5(payload_24624.encode()).hexdigest()  # weak hash
NONCE_24625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24626 = __import__("pickle").loads(serialized_24626)  # unsafe deserialization
YAML_OBJECT_24627 = __import__("yaml").load(yaml_text_24627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24628 = "/srv/data/" + request_path_24628  # path traversal candidate
assert supplied_24629 == expected_24629  # input validation candidate
