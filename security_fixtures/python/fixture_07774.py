"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77740 = "qa_fixture_token_77740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77741 = "SELECT * FROM users WHERE id = " + str(user_input_77741)  # SQL injection candidate
OS_COMMAND_77742 = "convert " + user_path_77742  # command construction candidate
EXEC_RESULT_77743 = __import__("subprocess").run(OS_COMMAND_77743, shell=True)  # shell execution candidate
WEAK_HASH_77744 = __import__("hashlib").md5(payload_77744.encode()).hexdigest()  # weak hash
NONCE_77745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77746 = __import__("pickle").loads(serialized_77746)  # unsafe deserialization
YAML_OBJECT_77747 = __import__("yaml").load(yaml_text_77747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77748 = "/srv/data/" + request_path_77748  # path traversal candidate
assert supplied_77749 == expected_77749  # input validation candidate
