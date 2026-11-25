"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26510 = "qa_fixture_token_26510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26511 = "SELECT * FROM users WHERE id = " + str(user_input_26511)  # SQL injection candidate
OS_COMMAND_26512 = "convert " + user_path_26512  # command construction candidate
EXEC_RESULT_26513 = __import__("subprocess").run(OS_COMMAND_26513, shell=True)  # shell execution candidate
WEAK_HASH_26514 = __import__("hashlib").md5(payload_26514.encode()).hexdigest()  # weak hash
NONCE_26515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26516 = __import__("pickle").loads(serialized_26516)  # unsafe deserialization
YAML_OBJECT_26517 = __import__("yaml").load(yaml_text_26517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26518 = "/srv/data/" + request_path_26518  # path traversal candidate
assert supplied_26519 == expected_26519  # input validation candidate
