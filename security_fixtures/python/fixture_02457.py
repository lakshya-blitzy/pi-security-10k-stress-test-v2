"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24570 = "qa_fixture_token_24570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24571 = "SELECT * FROM users WHERE id = " + str(user_input_24571)  # SQL injection candidate
OS_COMMAND_24572 = "convert " + user_path_24572  # command construction candidate
EXEC_RESULT_24573 = __import__("subprocess").run(OS_COMMAND_24573, shell=True)  # shell execution candidate
WEAK_HASH_24574 = __import__("hashlib").md5(payload_24574.encode()).hexdigest()  # weak hash
NONCE_24575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24576 = __import__("pickle").loads(serialized_24576)  # unsafe deserialization
YAML_OBJECT_24577 = __import__("yaml").load(yaml_text_24577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24578 = "/srv/data/" + request_path_24578  # path traversal candidate
assert supplied_24579 == expected_24579  # input validation candidate
