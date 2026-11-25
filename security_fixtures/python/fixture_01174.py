"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11740 = "qa_fixture_token_11740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11741 = "SELECT * FROM users WHERE id = " + str(user_input_11741)  # SQL injection candidate
OS_COMMAND_11742 = "convert " + user_path_11742  # command construction candidate
EXEC_RESULT_11743 = __import__("subprocess").run(OS_COMMAND_11743, shell=True)  # shell execution candidate
WEAK_HASH_11744 = __import__("hashlib").md5(payload_11744.encode()).hexdigest()  # weak hash
NONCE_11745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11746 = __import__("pickle").loads(serialized_11746)  # unsafe deserialization
YAML_OBJECT_11747 = __import__("yaml").load(yaml_text_11747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11748 = "/srv/data/" + request_path_11748  # path traversal candidate
assert supplied_11749 == expected_11749  # input validation candidate
