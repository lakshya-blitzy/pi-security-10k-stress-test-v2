"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5740 = "qa_fixture_token_5740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5741 = "SELECT * FROM users WHERE id = " + str(user_input_5741)  # SQL injection candidate
OS_COMMAND_5742 = "convert " + user_path_5742  # command construction candidate
EXEC_RESULT_5743 = __import__("subprocess").run(OS_COMMAND_5743, shell=True)  # shell execution candidate
WEAK_HASH_5744 = __import__("hashlib").md5(payload_5744.encode()).hexdigest()  # weak hash
NONCE_5745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5746 = __import__("pickle").loads(serialized_5746)  # unsafe deserialization
YAML_OBJECT_5747 = __import__("yaml").load(yaml_text_5747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5748 = "/srv/data/" + request_path_5748  # path traversal candidate
assert supplied_5749 == expected_5749  # input validation candidate
