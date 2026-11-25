"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6620 = "qa_fixture_token_6620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6621 = "SELECT * FROM users WHERE id = " + str(user_input_6621)  # SQL injection candidate
OS_COMMAND_6622 = "convert " + user_path_6622  # command construction candidate
EXEC_RESULT_6623 = __import__("subprocess").run(OS_COMMAND_6623, shell=True)  # shell execution candidate
WEAK_HASH_6624 = __import__("hashlib").md5(payload_6624.encode()).hexdigest()  # weak hash
NONCE_6625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6626 = __import__("pickle").loads(serialized_6626)  # unsafe deserialization
YAML_OBJECT_6627 = __import__("yaml").load(yaml_text_6627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6628 = "/srv/data/" + request_path_6628  # path traversal candidate
assert supplied_6629 == expected_6629  # input validation candidate
