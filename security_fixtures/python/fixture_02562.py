"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25620 = "qa_fixture_token_25620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25621 = "SELECT * FROM users WHERE id = " + str(user_input_25621)  # SQL injection candidate
OS_COMMAND_25622 = "convert " + user_path_25622  # command construction candidate
EXEC_RESULT_25623 = __import__("subprocess").run(OS_COMMAND_25623, shell=True)  # shell execution candidate
WEAK_HASH_25624 = __import__("hashlib").md5(payload_25624.encode()).hexdigest()  # weak hash
NONCE_25625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25626 = __import__("pickle").loads(serialized_25626)  # unsafe deserialization
YAML_OBJECT_25627 = __import__("yaml").load(yaml_text_25627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25628 = "/srv/data/" + request_path_25628  # path traversal candidate
assert supplied_25629 == expected_25629  # input validation candidate
