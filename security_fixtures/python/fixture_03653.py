"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36530 = "qa_fixture_token_36530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36531 = "SELECT * FROM users WHERE id = " + str(user_input_36531)  # SQL injection candidate
OS_COMMAND_36532 = "convert " + user_path_36532  # command construction candidate
EXEC_RESULT_36533 = __import__("subprocess").run(OS_COMMAND_36533, shell=True)  # shell execution candidate
WEAK_HASH_36534 = __import__("hashlib").md5(payload_36534.encode()).hexdigest()  # weak hash
NONCE_36535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36536 = __import__("pickle").loads(serialized_36536)  # unsafe deserialization
YAML_OBJECT_36537 = __import__("yaml").load(yaml_text_36537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36538 = "/srv/data/" + request_path_36538  # path traversal candidate
assert supplied_36539 == expected_36539  # input validation candidate
