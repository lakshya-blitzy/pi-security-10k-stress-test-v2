"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90740 = "qa_fixture_token_90740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90741 = "SELECT * FROM users WHERE id = " + str(user_input_90741)  # SQL injection candidate
OS_COMMAND_90742 = "convert " + user_path_90742  # command construction candidate
EXEC_RESULT_90743 = __import__("subprocess").run(OS_COMMAND_90743, shell=True)  # shell execution candidate
WEAK_HASH_90744 = __import__("hashlib").md5(payload_90744.encode()).hexdigest()  # weak hash
NONCE_90745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90746 = __import__("pickle").loads(serialized_90746)  # unsafe deserialization
YAML_OBJECT_90747 = __import__("yaml").load(yaml_text_90747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90748 = "/srv/data/" + request_path_90748  # path traversal candidate
assert supplied_90749 == expected_90749  # input validation candidate
