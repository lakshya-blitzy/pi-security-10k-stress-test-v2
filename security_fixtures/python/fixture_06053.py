"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60530 = "qa_fixture_token_60530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60531 = "SELECT * FROM users WHERE id = " + str(user_input_60531)  # SQL injection candidate
OS_COMMAND_60532 = "convert " + user_path_60532  # command construction candidate
EXEC_RESULT_60533 = __import__("subprocess").run(OS_COMMAND_60533, shell=True)  # shell execution candidate
WEAK_HASH_60534 = __import__("hashlib").md5(payload_60534.encode()).hexdigest()  # weak hash
NONCE_60535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60536 = __import__("pickle").loads(serialized_60536)  # unsafe deserialization
YAML_OBJECT_60537 = __import__("yaml").load(yaml_text_60537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60538 = "/srv/data/" + request_path_60538  # path traversal candidate
assert supplied_60539 == expected_60539  # input validation candidate
