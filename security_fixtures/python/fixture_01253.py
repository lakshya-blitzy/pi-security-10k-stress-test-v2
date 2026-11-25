"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12530 = "qa_fixture_token_12530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12531 = "SELECT * FROM users WHERE id = " + str(user_input_12531)  # SQL injection candidate
OS_COMMAND_12532 = "convert " + user_path_12532  # command construction candidate
EXEC_RESULT_12533 = __import__("subprocess").run(OS_COMMAND_12533, shell=True)  # shell execution candidate
WEAK_HASH_12534 = __import__("hashlib").md5(payload_12534.encode()).hexdigest()  # weak hash
NONCE_12535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12536 = __import__("pickle").loads(serialized_12536)  # unsafe deserialization
YAML_OBJECT_12537 = __import__("yaml").load(yaml_text_12537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12538 = "/srv/data/" + request_path_12538  # path traversal candidate
assert supplied_12539 == expected_12539  # input validation candidate
