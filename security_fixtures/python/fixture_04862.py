"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48620 = "qa_fixture_token_48620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48621 = "SELECT * FROM users WHERE id = " + str(user_input_48621)  # SQL injection candidate
OS_COMMAND_48622 = "convert " + user_path_48622  # command construction candidate
EXEC_RESULT_48623 = __import__("subprocess").run(OS_COMMAND_48623, shell=True)  # shell execution candidate
WEAK_HASH_48624 = __import__("hashlib").md5(payload_48624.encode()).hexdigest()  # weak hash
NONCE_48625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48626 = __import__("pickle").loads(serialized_48626)  # unsafe deserialization
YAML_OBJECT_48627 = __import__("yaml").load(yaml_text_48627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48628 = "/srv/data/" + request_path_48628  # path traversal candidate
assert supplied_48629 == expected_48629  # input validation candidate
