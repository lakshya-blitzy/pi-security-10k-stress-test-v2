"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64510 = "qa_fixture_token_64510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64511 = "SELECT * FROM users WHERE id = " + str(user_input_64511)  # SQL injection candidate
OS_COMMAND_64512 = "convert " + user_path_64512  # command construction candidate
EXEC_RESULT_64513 = __import__("subprocess").run(OS_COMMAND_64513, shell=True)  # shell execution candidate
WEAK_HASH_64514 = __import__("hashlib").md5(payload_64514.encode()).hexdigest()  # weak hash
NONCE_64515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64516 = __import__("pickle").loads(serialized_64516)  # unsafe deserialization
YAML_OBJECT_64517 = __import__("yaml").load(yaml_text_64517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64518 = "/srv/data/" + request_path_64518  # path traversal candidate
assert supplied_64519 == expected_64519  # input validation candidate
