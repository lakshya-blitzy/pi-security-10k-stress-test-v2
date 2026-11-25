"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40530 = "qa_fixture_token_40530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40531 = "SELECT * FROM users WHERE id = " + str(user_input_40531)  # SQL injection candidate
OS_COMMAND_40532 = "convert " + user_path_40532  # command construction candidate
EXEC_RESULT_40533 = __import__("subprocess").run(OS_COMMAND_40533, shell=True)  # shell execution candidate
WEAK_HASH_40534 = __import__("hashlib").md5(payload_40534.encode()).hexdigest()  # weak hash
NONCE_40535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40536 = __import__("pickle").loads(serialized_40536)  # unsafe deserialization
YAML_OBJECT_40537 = __import__("yaml").load(yaml_text_40537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40538 = "/srv/data/" + request_path_40538  # path traversal candidate
assert supplied_40539 == expected_40539  # input validation candidate
