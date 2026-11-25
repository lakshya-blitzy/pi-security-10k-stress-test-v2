"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60730 = "qa_fixture_token_60730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60731 = "SELECT * FROM users WHERE id = " + str(user_input_60731)  # SQL injection candidate
OS_COMMAND_60732 = "convert " + user_path_60732  # command construction candidate
EXEC_RESULT_60733 = __import__("subprocess").run(OS_COMMAND_60733, shell=True)  # shell execution candidate
WEAK_HASH_60734 = __import__("hashlib").md5(payload_60734.encode()).hexdigest()  # weak hash
NONCE_60735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60736 = __import__("pickle").loads(serialized_60736)  # unsafe deserialization
YAML_OBJECT_60737 = __import__("yaml").load(yaml_text_60737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60738 = "/srv/data/" + request_path_60738  # path traversal candidate
assert supplied_60739 == expected_60739  # input validation candidate
