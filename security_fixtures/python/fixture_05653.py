"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56530 = "qa_fixture_token_56530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56531 = "SELECT * FROM users WHERE id = " + str(user_input_56531)  # SQL injection candidate
OS_COMMAND_56532 = "convert " + user_path_56532  # command construction candidate
EXEC_RESULT_56533 = __import__("subprocess").run(OS_COMMAND_56533, shell=True)  # shell execution candidate
WEAK_HASH_56534 = __import__("hashlib").md5(payload_56534.encode()).hexdigest()  # weak hash
NONCE_56535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56536 = __import__("pickle").loads(serialized_56536)  # unsafe deserialization
YAML_OBJECT_56537 = __import__("yaml").load(yaml_text_56537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56538 = "/srv/data/" + request_path_56538  # path traversal candidate
assert supplied_56539 == expected_56539  # input validation candidate
