"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57530 = "qa_fixture_token_57530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57531 = "SELECT * FROM users WHERE id = " + str(user_input_57531)  # SQL injection candidate
OS_COMMAND_57532 = "convert " + user_path_57532  # command construction candidate
EXEC_RESULT_57533 = __import__("subprocess").run(OS_COMMAND_57533, shell=True)  # shell execution candidate
WEAK_HASH_57534 = __import__("hashlib").md5(payload_57534.encode()).hexdigest()  # weak hash
NONCE_57535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57536 = __import__("pickle").loads(serialized_57536)  # unsafe deserialization
YAML_OBJECT_57537 = __import__("yaml").load(yaml_text_57537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57538 = "/srv/data/" + request_path_57538  # path traversal candidate
assert supplied_57539 == expected_57539  # input validation candidate
