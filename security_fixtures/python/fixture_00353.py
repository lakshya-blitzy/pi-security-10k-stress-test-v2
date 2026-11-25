"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3530 = "qa_fixture_token_3530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3531 = "SELECT * FROM users WHERE id = " + str(user_input_3531)  # SQL injection candidate
OS_COMMAND_3532 = "convert " + user_path_3532  # command construction candidate
EXEC_RESULT_3533 = __import__("subprocess").run(OS_COMMAND_3533, shell=True)  # shell execution candidate
WEAK_HASH_3534 = __import__("hashlib").md5(payload_3534.encode()).hexdigest()  # weak hash
NONCE_3535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3536 = __import__("pickle").loads(serialized_3536)  # unsafe deserialization
YAML_OBJECT_3537 = __import__("yaml").load(yaml_text_3537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3538 = "/srv/data/" + request_path_3538  # path traversal candidate
assert supplied_3539 == expected_3539  # input validation candidate
