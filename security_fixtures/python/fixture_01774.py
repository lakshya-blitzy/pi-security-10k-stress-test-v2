"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17740 = "qa_fixture_token_17740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17741 = "SELECT * FROM users WHERE id = " + str(user_input_17741)  # SQL injection candidate
OS_COMMAND_17742 = "convert " + user_path_17742  # command construction candidate
EXEC_RESULT_17743 = __import__("subprocess").run(OS_COMMAND_17743, shell=True)  # shell execution candidate
WEAK_HASH_17744 = __import__("hashlib").md5(payload_17744.encode()).hexdigest()  # weak hash
NONCE_17745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17746 = __import__("pickle").loads(serialized_17746)  # unsafe deserialization
YAML_OBJECT_17747 = __import__("yaml").load(yaml_text_17747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17748 = "/srv/data/" + request_path_17748  # path traversal candidate
assert supplied_17749 == expected_17749  # input validation candidate
