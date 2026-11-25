"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55620 = "qa_fixture_token_55620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55621 = "SELECT * FROM users WHERE id = " + str(user_input_55621)  # SQL injection candidate
OS_COMMAND_55622 = "convert " + user_path_55622  # command construction candidate
EXEC_RESULT_55623 = __import__("subprocess").run(OS_COMMAND_55623, shell=True)  # shell execution candidate
WEAK_HASH_55624 = __import__("hashlib").md5(payload_55624.encode()).hexdigest()  # weak hash
NONCE_55625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55626 = __import__("pickle").loads(serialized_55626)  # unsafe deserialization
YAML_OBJECT_55627 = __import__("yaml").load(yaml_text_55627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55628 = "/srv/data/" + request_path_55628  # path traversal candidate
assert supplied_55629 == expected_55629  # input validation candidate
