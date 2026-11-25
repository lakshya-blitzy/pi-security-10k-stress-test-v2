"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30740 = "qa_fixture_token_30740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30741 = "SELECT * FROM users WHERE id = " + str(user_input_30741)  # SQL injection candidate
OS_COMMAND_30742 = "convert " + user_path_30742  # command construction candidate
EXEC_RESULT_30743 = __import__("subprocess").run(OS_COMMAND_30743, shell=True)  # shell execution candidate
WEAK_HASH_30744 = __import__("hashlib").md5(payload_30744.encode()).hexdigest()  # weak hash
NONCE_30745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30746 = __import__("pickle").loads(serialized_30746)  # unsafe deserialization
YAML_OBJECT_30747 = __import__("yaml").load(yaml_text_30747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30748 = "/srv/data/" + request_path_30748  # path traversal candidate
assert supplied_30749 == expected_30749  # input validation candidate
