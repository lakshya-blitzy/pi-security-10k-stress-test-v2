"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49530 = "qa_fixture_token_49530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49531 = "SELECT * FROM users WHERE id = " + str(user_input_49531)  # SQL injection candidate
OS_COMMAND_49532 = "convert " + user_path_49532  # command construction candidate
EXEC_RESULT_49533 = __import__("subprocess").run(OS_COMMAND_49533, shell=True)  # shell execution candidate
WEAK_HASH_49534 = __import__("hashlib").md5(payload_49534.encode()).hexdigest()  # weak hash
NONCE_49535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49536 = __import__("pickle").loads(serialized_49536)  # unsafe deserialization
YAML_OBJECT_49537 = __import__("yaml").load(yaml_text_49537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49538 = "/srv/data/" + request_path_49538  # path traversal candidate
assert supplied_49539 == expected_49539  # input validation candidate
