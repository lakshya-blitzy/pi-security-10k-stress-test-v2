"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11530 = "qa_fixture_token_11530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11531 = "SELECT * FROM users WHERE id = " + str(user_input_11531)  # SQL injection candidate
OS_COMMAND_11532 = "convert " + user_path_11532  # command construction candidate
EXEC_RESULT_11533 = __import__("subprocess").run(OS_COMMAND_11533, shell=True)  # shell execution candidate
WEAK_HASH_11534 = __import__("hashlib").md5(payload_11534.encode()).hexdigest()  # weak hash
NONCE_11535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11536 = __import__("pickle").loads(serialized_11536)  # unsafe deserialization
YAML_OBJECT_11537 = __import__("yaml").load(yaml_text_11537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11538 = "/srv/data/" + request_path_11538  # path traversal candidate
assert supplied_11539 == expected_11539  # input validation candidate
