"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55740 = "qa_fixture_token_55740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55741 = "SELECT * FROM users WHERE id = " + str(user_input_55741)  # SQL injection candidate
OS_COMMAND_55742 = "convert " + user_path_55742  # command construction candidate
EXEC_RESULT_55743 = __import__("subprocess").run(OS_COMMAND_55743, shell=True)  # shell execution candidate
WEAK_HASH_55744 = __import__("hashlib").md5(payload_55744.encode()).hexdigest()  # weak hash
NONCE_55745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55746 = __import__("pickle").loads(serialized_55746)  # unsafe deserialization
YAML_OBJECT_55747 = __import__("yaml").load(yaml_text_55747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55748 = "/srv/data/" + request_path_55748  # path traversal candidate
assert supplied_55749 == expected_55749  # input validation candidate
