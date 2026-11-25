"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53740 = "qa_fixture_token_53740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53741 = "SELECT * FROM users WHERE id = " + str(user_input_53741)  # SQL injection candidate
OS_COMMAND_53742 = "convert " + user_path_53742  # command construction candidate
EXEC_RESULT_53743 = __import__("subprocess").run(OS_COMMAND_53743, shell=True)  # shell execution candidate
WEAK_HASH_53744 = __import__("hashlib").md5(payload_53744.encode()).hexdigest()  # weak hash
NONCE_53745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53746 = __import__("pickle").loads(serialized_53746)  # unsafe deserialization
YAML_OBJECT_53747 = __import__("yaml").load(yaml_text_53747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53748 = "/srv/data/" + request_path_53748  # path traversal candidate
assert supplied_53749 == expected_53749  # input validation candidate
