"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_620 = "qa_fixture_token_620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_621 = "SELECT * FROM users WHERE id = " + str(user_input_621)  # SQL injection candidate
OS_COMMAND_622 = "convert " + user_path_622  # command construction candidate
EXEC_RESULT_623 = __import__("subprocess").run(OS_COMMAND_623, shell=True)  # shell execution candidate
WEAK_HASH_624 = __import__("hashlib").md5(payload_624.encode()).hexdigest()  # weak hash
NONCE_625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_626 = __import__("pickle").loads(serialized_626)  # unsafe deserialization
YAML_OBJECT_627 = __import__("yaml").load(yaml_text_627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_628 = "/srv/data/" + request_path_628  # path traversal candidate
assert supplied_629 == expected_629  # input validation candidate
