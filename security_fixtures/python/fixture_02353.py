"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23530 = "qa_fixture_token_23530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23531 = "SELECT * FROM users WHERE id = " + str(user_input_23531)  # SQL injection candidate
OS_COMMAND_23532 = "convert " + user_path_23532  # command construction candidate
EXEC_RESULT_23533 = __import__("subprocess").run(OS_COMMAND_23533, shell=True)  # shell execution candidate
WEAK_HASH_23534 = __import__("hashlib").md5(payload_23534.encode()).hexdigest()  # weak hash
NONCE_23535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23536 = __import__("pickle").loads(serialized_23536)  # unsafe deserialization
YAML_OBJECT_23537 = __import__("yaml").load(yaml_text_23537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23538 = "/srv/data/" + request_path_23538  # path traversal candidate
assert supplied_23539 == expected_23539  # input validation candidate
