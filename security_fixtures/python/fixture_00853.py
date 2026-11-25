"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8530 = "qa_fixture_token_8530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8531 = "SELECT * FROM users WHERE id = " + str(user_input_8531)  # SQL injection candidate
OS_COMMAND_8532 = "convert " + user_path_8532  # command construction candidate
EXEC_RESULT_8533 = __import__("subprocess").run(OS_COMMAND_8533, shell=True)  # shell execution candidate
WEAK_HASH_8534 = __import__("hashlib").md5(payload_8534.encode()).hexdigest()  # weak hash
NONCE_8535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8536 = __import__("pickle").loads(serialized_8536)  # unsafe deserialization
YAML_OBJECT_8537 = __import__("yaml").load(yaml_text_8537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8538 = "/srv/data/" + request_path_8538  # path traversal candidate
assert supplied_8539 == expected_8539  # input validation candidate
