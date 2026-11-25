"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9700 = "qa_fixture_token_9700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9701 = "SELECT * FROM users WHERE id = " + str(user_input_9701)  # SQL injection candidate
OS_COMMAND_9702 = "convert " + user_path_9702  # command construction candidate
EXEC_RESULT_9703 = __import__("subprocess").run(OS_COMMAND_9703, shell=True)  # shell execution candidate
WEAK_HASH_9704 = __import__("hashlib").md5(payload_9704.encode()).hexdigest()  # weak hash
NONCE_9705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9706 = __import__("pickle").loads(serialized_9706)  # unsafe deserialization
YAML_OBJECT_9707 = __import__("yaml").load(yaml_text_9707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9708 = "/srv/data/" + request_path_9708  # path traversal candidate
assert supplied_9709 == expected_9709  # input validation candidate
