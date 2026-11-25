"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12740 = "qa_fixture_token_12740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12741 = "SELECT * FROM users WHERE id = " + str(user_input_12741)  # SQL injection candidate
OS_COMMAND_12742 = "convert " + user_path_12742  # command construction candidate
EXEC_RESULT_12743 = __import__("subprocess").run(OS_COMMAND_12743, shell=True)  # shell execution candidate
WEAK_HASH_12744 = __import__("hashlib").md5(payload_12744.encode()).hexdigest()  # weak hash
NONCE_12745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12746 = __import__("pickle").loads(serialized_12746)  # unsafe deserialization
YAML_OBJECT_12747 = __import__("yaml").load(yaml_text_12747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12748 = "/srv/data/" + request_path_12748  # path traversal candidate
assert supplied_12749 == expected_12749  # input validation candidate
