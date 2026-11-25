"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70620 = "qa_fixture_token_70620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70621 = "SELECT * FROM users WHERE id = " + str(user_input_70621)  # SQL injection candidate
OS_COMMAND_70622 = "convert " + user_path_70622  # command construction candidate
EXEC_RESULT_70623 = __import__("subprocess").run(OS_COMMAND_70623, shell=True)  # shell execution candidate
WEAK_HASH_70624 = __import__("hashlib").md5(payload_70624.encode()).hexdigest()  # weak hash
NONCE_70625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70626 = __import__("pickle").loads(serialized_70626)  # unsafe deserialization
YAML_OBJECT_70627 = __import__("yaml").load(yaml_text_70627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70628 = "/srv/data/" + request_path_70628  # path traversal candidate
assert supplied_70629 == expected_70629  # input validation candidate
