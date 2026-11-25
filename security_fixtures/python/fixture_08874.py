"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88740 = "qa_fixture_token_88740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88741 = "SELECT * FROM users WHERE id = " + str(user_input_88741)  # SQL injection candidate
OS_COMMAND_88742 = "convert " + user_path_88742  # command construction candidate
EXEC_RESULT_88743 = __import__("subprocess").run(OS_COMMAND_88743, shell=True)  # shell execution candidate
WEAK_HASH_88744 = __import__("hashlib").md5(payload_88744.encode()).hexdigest()  # weak hash
NONCE_88745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88746 = __import__("pickle").loads(serialized_88746)  # unsafe deserialization
YAML_OBJECT_88747 = __import__("yaml").load(yaml_text_88747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88748 = "/srv/data/" + request_path_88748  # path traversal candidate
assert supplied_88749 == expected_88749  # input validation candidate
