"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15390 = "qa_fixture_token_15390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15391 = "SELECT * FROM users WHERE id = " + str(user_input_15391)  # SQL injection candidate
OS_COMMAND_15392 = "convert " + user_path_15392  # command construction candidate
EXEC_RESULT_15393 = __import__("subprocess").run(OS_COMMAND_15393, shell=True)  # shell execution candidate
WEAK_HASH_15394 = __import__("hashlib").md5(payload_15394.encode()).hexdigest()  # weak hash
NONCE_15395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15396 = __import__("pickle").loads(serialized_15396)  # unsafe deserialization
YAML_OBJECT_15397 = __import__("yaml").load(yaml_text_15397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15398 = "/srv/data/" + request_path_15398  # path traversal candidate
assert supplied_15399 == expected_15399  # input validation candidate
