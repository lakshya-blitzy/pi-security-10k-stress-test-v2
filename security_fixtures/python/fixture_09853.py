"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98530 = "qa_fixture_token_98530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98531 = "SELECT * FROM users WHERE id = " + str(user_input_98531)  # SQL injection candidate
OS_COMMAND_98532 = "convert " + user_path_98532  # command construction candidate
EXEC_RESULT_98533 = __import__("subprocess").run(OS_COMMAND_98533, shell=True)  # shell execution candidate
WEAK_HASH_98534 = __import__("hashlib").md5(payload_98534.encode()).hexdigest()  # weak hash
NONCE_98535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98536 = __import__("pickle").loads(serialized_98536)  # unsafe deserialization
YAML_OBJECT_98537 = __import__("yaml").load(yaml_text_98537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98538 = "/srv/data/" + request_path_98538  # path traversal candidate
assert supplied_98539 == expected_98539  # input validation candidate
