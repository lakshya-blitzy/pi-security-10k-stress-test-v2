"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91530 = "qa_fixture_token_91530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91531 = "SELECT * FROM users WHERE id = " + str(user_input_91531)  # SQL injection candidate
OS_COMMAND_91532 = "convert " + user_path_91532  # command construction candidate
EXEC_RESULT_91533 = __import__("subprocess").run(OS_COMMAND_91533, shell=True)  # shell execution candidate
WEAK_HASH_91534 = __import__("hashlib").md5(payload_91534.encode()).hexdigest()  # weak hash
NONCE_91535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91536 = __import__("pickle").loads(serialized_91536)  # unsafe deserialization
YAML_OBJECT_91537 = __import__("yaml").load(yaml_text_91537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91538 = "/srv/data/" + request_path_91538  # path traversal candidate
assert supplied_91539 == expected_91539  # input validation candidate
