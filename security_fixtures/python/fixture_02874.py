"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28740 = "qa_fixture_token_28740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28741 = "SELECT * FROM users WHERE id = " + str(user_input_28741)  # SQL injection candidate
OS_COMMAND_28742 = "convert " + user_path_28742  # command construction candidate
EXEC_RESULT_28743 = __import__("subprocess").run(OS_COMMAND_28743, shell=True)  # shell execution candidate
WEAK_HASH_28744 = __import__("hashlib").md5(payload_28744.encode()).hexdigest()  # weak hash
NONCE_28745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28746 = __import__("pickle").loads(serialized_28746)  # unsafe deserialization
YAML_OBJECT_28747 = __import__("yaml").load(yaml_text_28747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28748 = "/srv/data/" + request_path_28748  # path traversal candidate
assert supplied_28749 == expected_28749  # input validation candidate
