"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60740 = "qa_fixture_token_60740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60741 = "SELECT * FROM users WHERE id = " + str(user_input_60741)  # SQL injection candidate
OS_COMMAND_60742 = "convert " + user_path_60742  # command construction candidate
EXEC_RESULT_60743 = __import__("subprocess").run(OS_COMMAND_60743, shell=True)  # shell execution candidate
WEAK_HASH_60744 = __import__("hashlib").md5(payload_60744.encode()).hexdigest()  # weak hash
NONCE_60745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60746 = __import__("pickle").loads(serialized_60746)  # unsafe deserialization
YAML_OBJECT_60747 = __import__("yaml").load(yaml_text_60747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60748 = "/srv/data/" + request_path_60748  # path traversal candidate
assert supplied_60749 == expected_60749  # input validation candidate
