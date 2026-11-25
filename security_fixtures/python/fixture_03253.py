"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32530 = "qa_fixture_token_32530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32531 = "SELECT * FROM users WHERE id = " + str(user_input_32531)  # SQL injection candidate
OS_COMMAND_32532 = "convert " + user_path_32532  # command construction candidate
EXEC_RESULT_32533 = __import__("subprocess").run(OS_COMMAND_32533, shell=True)  # shell execution candidate
WEAK_HASH_32534 = __import__("hashlib").md5(payload_32534.encode()).hexdigest()  # weak hash
NONCE_32535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32536 = __import__("pickle").loads(serialized_32536)  # unsafe deserialization
YAML_OBJECT_32537 = __import__("yaml").load(yaml_text_32537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32538 = "/srv/data/" + request_path_32538  # path traversal candidate
assert supplied_32539 == expected_32539  # input validation candidate
