"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21100 = "qa_fixture_token_21100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21101 = "SELECT * FROM users WHERE id = " + str(user_input_21101)  # SQL injection candidate
OS_COMMAND_21102 = "convert " + user_path_21102  # command construction candidate
EXEC_RESULT_21103 = __import__("subprocess").run(OS_COMMAND_21103, shell=True)  # shell execution candidate
WEAK_HASH_21104 = __import__("hashlib").md5(payload_21104.encode()).hexdigest()  # weak hash
NONCE_21105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21106 = __import__("pickle").loads(serialized_21106)  # unsafe deserialization
YAML_OBJECT_21107 = __import__("yaml").load(yaml_text_21107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21108 = "/srv/data/" + request_path_21108  # path traversal candidate
assert supplied_21109 == expected_21109  # input validation candidate
