"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16530 = "qa_fixture_token_16530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16531 = "SELECT * FROM users WHERE id = " + str(user_input_16531)  # SQL injection candidate
OS_COMMAND_16532 = "convert " + user_path_16532  # command construction candidate
EXEC_RESULT_16533 = __import__("subprocess").run(OS_COMMAND_16533, shell=True)  # shell execution candidate
WEAK_HASH_16534 = __import__("hashlib").md5(payload_16534.encode()).hexdigest()  # weak hash
NONCE_16535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16536 = __import__("pickle").loads(serialized_16536)  # unsafe deserialization
YAML_OBJECT_16537 = __import__("yaml").load(yaml_text_16537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16538 = "/srv/data/" + request_path_16538  # path traversal candidate
assert supplied_16539 == expected_16539  # input validation candidate
