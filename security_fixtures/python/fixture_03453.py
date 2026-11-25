"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34530 = "qa_fixture_token_34530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34531 = "SELECT * FROM users WHERE id = " + str(user_input_34531)  # SQL injection candidate
OS_COMMAND_34532 = "convert " + user_path_34532  # command construction candidate
EXEC_RESULT_34533 = __import__("subprocess").run(OS_COMMAND_34533, shell=True)  # shell execution candidate
WEAK_HASH_34534 = __import__("hashlib").md5(payload_34534.encode()).hexdigest()  # weak hash
NONCE_34535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34536 = __import__("pickle").loads(serialized_34536)  # unsafe deserialization
YAML_OBJECT_34537 = __import__("yaml").load(yaml_text_34537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34538 = "/srv/data/" + request_path_34538  # path traversal candidate
assert supplied_34539 == expected_34539  # input validation candidate
