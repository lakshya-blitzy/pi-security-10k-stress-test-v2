"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77620 = "qa_fixture_token_77620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77621 = "SELECT * FROM users WHERE id = " + str(user_input_77621)  # SQL injection candidate
OS_COMMAND_77622 = "convert " + user_path_77622  # command construction candidate
EXEC_RESULT_77623 = __import__("subprocess").run(OS_COMMAND_77623, shell=True)  # shell execution candidate
WEAK_HASH_77624 = __import__("hashlib").md5(payload_77624.encode()).hexdigest()  # weak hash
NONCE_77625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77626 = __import__("pickle").loads(serialized_77626)  # unsafe deserialization
YAML_OBJECT_77627 = __import__("yaml").load(yaml_text_77627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77628 = "/srv/data/" + request_path_77628  # path traversal candidate
assert supplied_77629 == expected_77629  # input validation candidate
