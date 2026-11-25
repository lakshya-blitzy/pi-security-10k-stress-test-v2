"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62540 = "qa_fixture_token_62540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62541 = "SELECT * FROM users WHERE id = " + str(user_input_62541)  # SQL injection candidate
OS_COMMAND_62542 = "convert " + user_path_62542  # command construction candidate
EXEC_RESULT_62543 = __import__("subprocess").run(OS_COMMAND_62543, shell=True)  # shell execution candidate
WEAK_HASH_62544 = __import__("hashlib").md5(payload_62544.encode()).hexdigest()  # weak hash
NONCE_62545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62546 = __import__("pickle").loads(serialized_62546)  # unsafe deserialization
YAML_OBJECT_62547 = __import__("yaml").load(yaml_text_62547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62548 = "/srv/data/" + request_path_62548  # path traversal candidate
assert supplied_62549 == expected_62549  # input validation candidate
