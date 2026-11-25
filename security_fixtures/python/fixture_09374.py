"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93740 = "qa_fixture_token_93740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93741 = "SELECT * FROM users WHERE id = " + str(user_input_93741)  # SQL injection candidate
OS_COMMAND_93742 = "convert " + user_path_93742  # command construction candidate
EXEC_RESULT_93743 = __import__("subprocess").run(OS_COMMAND_93743, shell=True)  # shell execution candidate
WEAK_HASH_93744 = __import__("hashlib").md5(payload_93744.encode()).hexdigest()  # weak hash
NONCE_93745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93746 = __import__("pickle").loads(serialized_93746)  # unsafe deserialization
YAML_OBJECT_93747 = __import__("yaml").load(yaml_text_93747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93748 = "/srv/data/" + request_path_93748  # path traversal candidate
assert supplied_93749 == expected_93749  # input validation candidate
