"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92530 = "qa_fixture_token_92530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92531 = "SELECT * FROM users WHERE id = " + str(user_input_92531)  # SQL injection candidate
OS_COMMAND_92532 = "convert " + user_path_92532  # command construction candidate
EXEC_RESULT_92533 = __import__("subprocess").run(OS_COMMAND_92533, shell=True)  # shell execution candidate
WEAK_HASH_92534 = __import__("hashlib").md5(payload_92534.encode()).hexdigest()  # weak hash
NONCE_92535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92536 = __import__("pickle").loads(serialized_92536)  # unsafe deserialization
YAML_OBJECT_92537 = __import__("yaml").load(yaml_text_92537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92538 = "/srv/data/" + request_path_92538  # path traversal candidate
assert supplied_92539 == expected_92539  # input validation candidate
