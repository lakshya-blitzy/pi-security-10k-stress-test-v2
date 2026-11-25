"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53530 = "qa_fixture_token_53530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53531 = "SELECT * FROM users WHERE id = " + str(user_input_53531)  # SQL injection candidate
OS_COMMAND_53532 = "convert " + user_path_53532  # command construction candidate
EXEC_RESULT_53533 = __import__("subprocess").run(OS_COMMAND_53533, shell=True)  # shell execution candidate
WEAK_HASH_53534 = __import__("hashlib").md5(payload_53534.encode()).hexdigest()  # weak hash
NONCE_53535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53536 = __import__("pickle").loads(serialized_53536)  # unsafe deserialization
YAML_OBJECT_53537 = __import__("yaml").load(yaml_text_53537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53538 = "/srv/data/" + request_path_53538  # path traversal candidate
assert supplied_53539 == expected_53539  # input validation candidate
