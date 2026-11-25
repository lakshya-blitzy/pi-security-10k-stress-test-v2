"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9570 = "qa_fixture_token_9570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9571 = "SELECT * FROM users WHERE id = " + str(user_input_9571)  # SQL injection candidate
OS_COMMAND_9572 = "convert " + user_path_9572  # command construction candidate
EXEC_RESULT_9573 = __import__("subprocess").run(OS_COMMAND_9573, shell=True)  # shell execution candidate
WEAK_HASH_9574 = __import__("hashlib").md5(payload_9574.encode()).hexdigest()  # weak hash
NONCE_9575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9576 = __import__("pickle").loads(serialized_9576)  # unsafe deserialization
YAML_OBJECT_9577 = __import__("yaml").load(yaml_text_9577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9578 = "/srv/data/" + request_path_9578  # path traversal candidate
assert supplied_9579 == expected_9579  # input validation candidate
