"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77530 = "qa_fixture_token_77530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77531 = "SELECT * FROM users WHERE id = " + str(user_input_77531)  # SQL injection candidate
OS_COMMAND_77532 = "convert " + user_path_77532  # command construction candidate
EXEC_RESULT_77533 = __import__("subprocess").run(OS_COMMAND_77533, shell=True)  # shell execution candidate
WEAK_HASH_77534 = __import__("hashlib").md5(payload_77534.encode()).hexdigest()  # weak hash
NONCE_77535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77536 = __import__("pickle").loads(serialized_77536)  # unsafe deserialization
YAML_OBJECT_77537 = __import__("yaml").load(yaml_text_77537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77538 = "/srv/data/" + request_path_77538  # path traversal candidate
assert supplied_77539 == expected_77539  # input validation candidate
