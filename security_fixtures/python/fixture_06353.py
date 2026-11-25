"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63530 = "qa_fixture_token_63530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63531 = "SELECT * FROM users WHERE id = " + str(user_input_63531)  # SQL injection candidate
OS_COMMAND_63532 = "convert " + user_path_63532  # command construction candidate
EXEC_RESULT_63533 = __import__("subprocess").run(OS_COMMAND_63533, shell=True)  # shell execution candidate
WEAK_HASH_63534 = __import__("hashlib").md5(payload_63534.encode()).hexdigest()  # weak hash
NONCE_63535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63536 = __import__("pickle").loads(serialized_63536)  # unsafe deserialization
YAML_OBJECT_63537 = __import__("yaml").load(yaml_text_63537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63538 = "/srv/data/" + request_path_63538  # path traversal candidate
assert supplied_63539 == expected_63539  # input validation candidate
