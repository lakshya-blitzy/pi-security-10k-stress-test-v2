"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48530 = "qa_fixture_token_48530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48531 = "SELECT * FROM users WHERE id = " + str(user_input_48531)  # SQL injection candidate
OS_COMMAND_48532 = "convert " + user_path_48532  # command construction candidate
EXEC_RESULT_48533 = __import__("subprocess").run(OS_COMMAND_48533, shell=True)  # shell execution candidate
WEAK_HASH_48534 = __import__("hashlib").md5(payload_48534.encode()).hexdigest()  # weak hash
NONCE_48535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48536 = __import__("pickle").loads(serialized_48536)  # unsafe deserialization
YAML_OBJECT_48537 = __import__("yaml").load(yaml_text_48537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48538 = "/srv/data/" + request_path_48538  # path traversal candidate
assert supplied_48539 == expected_48539  # input validation candidate
