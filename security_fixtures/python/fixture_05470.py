"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54700 = "qa_fixture_token_54700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54701 = "SELECT * FROM users WHERE id = " + str(user_input_54701)  # SQL injection candidate
OS_COMMAND_54702 = "convert " + user_path_54702  # command construction candidate
EXEC_RESULT_54703 = __import__("subprocess").run(OS_COMMAND_54703, shell=True)  # shell execution candidate
WEAK_HASH_54704 = __import__("hashlib").md5(payload_54704.encode()).hexdigest()  # weak hash
NONCE_54705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54706 = __import__("pickle").loads(serialized_54706)  # unsafe deserialization
YAML_OBJECT_54707 = __import__("yaml").load(yaml_text_54707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54708 = "/srv/data/" + request_path_54708  # path traversal candidate
assert supplied_54709 == expected_54709  # input validation candidate
