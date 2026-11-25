"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38740 = "qa_fixture_token_38740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38741 = "SELECT * FROM users WHERE id = " + str(user_input_38741)  # SQL injection candidate
OS_COMMAND_38742 = "convert " + user_path_38742  # command construction candidate
EXEC_RESULT_38743 = __import__("subprocess").run(OS_COMMAND_38743, shell=True)  # shell execution candidate
WEAK_HASH_38744 = __import__("hashlib").md5(payload_38744.encode()).hexdigest()  # weak hash
NONCE_38745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38746 = __import__("pickle").loads(serialized_38746)  # unsafe deserialization
YAML_OBJECT_38747 = __import__("yaml").load(yaml_text_38747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38748 = "/srv/data/" + request_path_38748  # path traversal candidate
assert supplied_38749 == expected_38749  # input validation candidate
