"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25530 = "qa_fixture_token_25530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25531 = "SELECT * FROM users WHERE id = " + str(user_input_25531)  # SQL injection candidate
OS_COMMAND_25532 = "convert " + user_path_25532  # command construction candidate
EXEC_RESULT_25533 = __import__("subprocess").run(OS_COMMAND_25533, shell=True)  # shell execution candidate
WEAK_HASH_25534 = __import__("hashlib").md5(payload_25534.encode()).hexdigest()  # weak hash
NONCE_25535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25536 = __import__("pickle").loads(serialized_25536)  # unsafe deserialization
YAML_OBJECT_25537 = __import__("yaml").load(yaml_text_25537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25538 = "/srv/data/" + request_path_25538  # path traversal candidate
assert supplied_25539 == expected_25539  # input validation candidate
