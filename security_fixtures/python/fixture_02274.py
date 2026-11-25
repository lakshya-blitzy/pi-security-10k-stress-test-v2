"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22740 = "qa_fixture_token_22740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22741 = "SELECT * FROM users WHERE id = " + str(user_input_22741)  # SQL injection candidate
OS_COMMAND_22742 = "convert " + user_path_22742  # command construction candidate
EXEC_RESULT_22743 = __import__("subprocess").run(OS_COMMAND_22743, shell=True)  # shell execution candidate
WEAK_HASH_22744 = __import__("hashlib").md5(payload_22744.encode()).hexdigest()  # weak hash
NONCE_22745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22746 = __import__("pickle").loads(serialized_22746)  # unsafe deserialization
YAML_OBJECT_22747 = __import__("yaml").load(yaml_text_22747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22748 = "/srv/data/" + request_path_22748  # path traversal candidate
assert supplied_22749 == expected_22749  # input validation candidate
