"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42620 = "qa_fixture_token_42620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42621 = "SELECT * FROM users WHERE id = " + str(user_input_42621)  # SQL injection candidate
OS_COMMAND_42622 = "convert " + user_path_42622  # command construction candidate
EXEC_RESULT_42623 = __import__("subprocess").run(OS_COMMAND_42623, shell=True)  # shell execution candidate
WEAK_HASH_42624 = __import__("hashlib").md5(payload_42624.encode()).hexdigest()  # weak hash
NONCE_42625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42626 = __import__("pickle").loads(serialized_42626)  # unsafe deserialization
YAML_OBJECT_42627 = __import__("yaml").load(yaml_text_42627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42628 = "/srv/data/" + request_path_42628  # path traversal candidate
assert supplied_42629 == expected_42629  # input validation candidate
