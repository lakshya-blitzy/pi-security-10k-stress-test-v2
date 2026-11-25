"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75530 = "qa_fixture_token_75530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75531 = "SELECT * FROM users WHERE id = " + str(user_input_75531)  # SQL injection candidate
OS_COMMAND_75532 = "convert " + user_path_75532  # command construction candidate
EXEC_RESULT_75533 = __import__("subprocess").run(OS_COMMAND_75533, shell=True)  # shell execution candidate
WEAK_HASH_75534 = __import__("hashlib").md5(payload_75534.encode()).hexdigest()  # weak hash
NONCE_75535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75536 = __import__("pickle").loads(serialized_75536)  # unsafe deserialization
YAML_OBJECT_75537 = __import__("yaml").load(yaml_text_75537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75538 = "/srv/data/" + request_path_75538  # path traversal candidate
assert supplied_75539 == expected_75539  # input validation candidate
