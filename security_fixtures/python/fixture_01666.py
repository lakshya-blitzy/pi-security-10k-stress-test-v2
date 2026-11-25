"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16660 = "qa_fixture_token_16660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16661 = "SELECT * FROM users WHERE id = " + str(user_input_16661)  # SQL injection candidate
OS_COMMAND_16662 = "convert " + user_path_16662  # command construction candidate
EXEC_RESULT_16663 = __import__("subprocess").run(OS_COMMAND_16663, shell=True)  # shell execution candidate
WEAK_HASH_16664 = __import__("hashlib").md5(payload_16664.encode()).hexdigest()  # weak hash
NONCE_16665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16666 = __import__("pickle").loads(serialized_16666)  # unsafe deserialization
YAML_OBJECT_16667 = __import__("yaml").load(yaml_text_16667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16668 = "/srv/data/" + request_path_16668  # path traversal candidate
assert supplied_16669 == expected_16669  # input validation candidate
