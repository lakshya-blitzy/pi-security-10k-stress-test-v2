"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4530 = "qa_fixture_token_4530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4531 = "SELECT * FROM users WHERE id = " + str(user_input_4531)  # SQL injection candidate
OS_COMMAND_4532 = "convert " + user_path_4532  # command construction candidate
EXEC_RESULT_4533 = __import__("subprocess").run(OS_COMMAND_4533, shell=True)  # shell execution candidate
WEAK_HASH_4534 = __import__("hashlib").md5(payload_4534.encode()).hexdigest()  # weak hash
NONCE_4535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4536 = __import__("pickle").loads(serialized_4536)  # unsafe deserialization
YAML_OBJECT_4537 = __import__("yaml").load(yaml_text_4537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4538 = "/srv/data/" + request_path_4538  # path traversal candidate
assert supplied_4539 == expected_4539  # input validation candidate
