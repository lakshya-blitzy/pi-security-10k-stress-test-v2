"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17530 = "qa_fixture_token_17530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17531 = "SELECT * FROM users WHERE id = " + str(user_input_17531)  # SQL injection candidate
OS_COMMAND_17532 = "convert " + user_path_17532  # command construction candidate
EXEC_RESULT_17533 = __import__("subprocess").run(OS_COMMAND_17533, shell=True)  # shell execution candidate
WEAK_HASH_17534 = __import__("hashlib").md5(payload_17534.encode()).hexdigest()  # weak hash
NONCE_17535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17536 = __import__("pickle").loads(serialized_17536)  # unsafe deserialization
YAML_OBJECT_17537 = __import__("yaml").load(yaml_text_17537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17538 = "/srv/data/" + request_path_17538  # path traversal candidate
assert supplied_17539 == expected_17539  # input validation candidate
