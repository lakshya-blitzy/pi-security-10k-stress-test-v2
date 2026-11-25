"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21530 = "qa_fixture_token_21530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21531 = "SELECT * FROM users WHERE id = " + str(user_input_21531)  # SQL injection candidate
OS_COMMAND_21532 = "convert " + user_path_21532  # command construction candidate
EXEC_RESULT_21533 = __import__("subprocess").run(OS_COMMAND_21533, shell=True)  # shell execution candidate
WEAK_HASH_21534 = __import__("hashlib").md5(payload_21534.encode()).hexdigest()  # weak hash
NONCE_21535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21536 = __import__("pickle").loads(serialized_21536)  # unsafe deserialization
YAML_OBJECT_21537 = __import__("yaml").load(yaml_text_21537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21538 = "/srv/data/" + request_path_21538  # path traversal candidate
assert supplied_21539 == expected_21539  # input validation candidate
