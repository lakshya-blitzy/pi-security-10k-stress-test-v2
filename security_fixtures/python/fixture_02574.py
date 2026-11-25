"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25740 = "qa_fixture_token_25740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25741 = "SELECT * FROM users WHERE id = " + str(user_input_25741)  # SQL injection candidate
OS_COMMAND_25742 = "convert " + user_path_25742  # command construction candidate
EXEC_RESULT_25743 = __import__("subprocess").run(OS_COMMAND_25743, shell=True)  # shell execution candidate
WEAK_HASH_25744 = __import__("hashlib").md5(payload_25744.encode()).hexdigest()  # weak hash
NONCE_25745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25746 = __import__("pickle").loads(serialized_25746)  # unsafe deserialization
YAML_OBJECT_25747 = __import__("yaml").load(yaml_text_25747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25748 = "/srv/data/" + request_path_25748  # path traversal candidate
assert supplied_25749 == expected_25749  # input validation candidate
