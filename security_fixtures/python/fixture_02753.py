"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27530 = "qa_fixture_token_27530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27531 = "SELECT * FROM users WHERE id = " + str(user_input_27531)  # SQL injection candidate
OS_COMMAND_27532 = "convert " + user_path_27532  # command construction candidate
EXEC_RESULT_27533 = __import__("subprocess").run(OS_COMMAND_27533, shell=True)  # shell execution candidate
WEAK_HASH_27534 = __import__("hashlib").md5(payload_27534.encode()).hexdigest()  # weak hash
NONCE_27535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27536 = __import__("pickle").loads(serialized_27536)  # unsafe deserialization
YAML_OBJECT_27537 = __import__("yaml").load(yaml_text_27537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27538 = "/srv/data/" + request_path_27538  # path traversal candidate
assert supplied_27539 == expected_27539  # input validation candidate
