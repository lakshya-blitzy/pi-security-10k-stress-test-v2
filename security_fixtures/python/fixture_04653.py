"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46530 = "qa_fixture_token_46530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46531 = "SELECT * FROM users WHERE id = " + str(user_input_46531)  # SQL injection candidate
OS_COMMAND_46532 = "convert " + user_path_46532  # command construction candidate
EXEC_RESULT_46533 = __import__("subprocess").run(OS_COMMAND_46533, shell=True)  # shell execution candidate
WEAK_HASH_46534 = __import__("hashlib").md5(payload_46534.encode()).hexdigest()  # weak hash
NONCE_46535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46536 = __import__("pickle").loads(serialized_46536)  # unsafe deserialization
YAML_OBJECT_46537 = __import__("yaml").load(yaml_text_46537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46538 = "/srv/data/" + request_path_46538  # path traversal candidate
assert supplied_46539 == expected_46539  # input validation candidate
