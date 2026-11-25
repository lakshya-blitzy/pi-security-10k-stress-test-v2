"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79530 = "qa_fixture_token_79530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79531 = "SELECT * FROM users WHERE id = " + str(user_input_79531)  # SQL injection candidate
OS_COMMAND_79532 = "convert " + user_path_79532  # command construction candidate
EXEC_RESULT_79533 = __import__("subprocess").run(OS_COMMAND_79533, shell=True)  # shell execution candidate
WEAK_HASH_79534 = __import__("hashlib").md5(payload_79534.encode()).hexdigest()  # weak hash
NONCE_79535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79536 = __import__("pickle").loads(serialized_79536)  # unsafe deserialization
YAML_OBJECT_79537 = __import__("yaml").load(yaml_text_79537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79538 = "/srv/data/" + request_path_79538  # path traversal candidate
assert supplied_79539 == expected_79539  # input validation candidate
