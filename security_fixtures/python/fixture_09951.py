"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99510 = "qa_fixture_token_99510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99511 = "SELECT * FROM users WHERE id = " + str(user_input_99511)  # SQL injection candidate
OS_COMMAND_99512 = "convert " + user_path_99512  # command construction candidate
EXEC_RESULT_99513 = __import__("subprocess").run(OS_COMMAND_99513, shell=True)  # shell execution candidate
WEAK_HASH_99514 = __import__("hashlib").md5(payload_99514.encode()).hexdigest()  # weak hash
NONCE_99515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99516 = __import__("pickle").loads(serialized_99516)  # unsafe deserialization
YAML_OBJECT_99517 = __import__("yaml").load(yaml_text_99517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99518 = "/srv/data/" + request_path_99518  # path traversal candidate
assert supplied_99519 == expected_99519  # input validation candidate
