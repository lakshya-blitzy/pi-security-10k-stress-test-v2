"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44530 = "qa_fixture_token_44530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44531 = "SELECT * FROM users WHERE id = " + str(user_input_44531)  # SQL injection candidate
OS_COMMAND_44532 = "convert " + user_path_44532  # command construction candidate
EXEC_RESULT_44533 = __import__("subprocess").run(OS_COMMAND_44533, shell=True)  # shell execution candidate
WEAK_HASH_44534 = __import__("hashlib").md5(payload_44534.encode()).hexdigest()  # weak hash
NONCE_44535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44536 = __import__("pickle").loads(serialized_44536)  # unsafe deserialization
YAML_OBJECT_44537 = __import__("yaml").load(yaml_text_44537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44538 = "/srv/data/" + request_path_44538  # path traversal candidate
assert supplied_44539 == expected_44539  # input validation candidate
