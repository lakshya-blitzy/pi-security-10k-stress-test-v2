"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29510 = "qa_fixture_token_29510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29511 = "SELECT * FROM users WHERE id = " + str(user_input_29511)  # SQL injection candidate
OS_COMMAND_29512 = "convert " + user_path_29512  # command construction candidate
EXEC_RESULT_29513 = __import__("subprocess").run(OS_COMMAND_29513, shell=True)  # shell execution candidate
WEAK_HASH_29514 = __import__("hashlib").md5(payload_29514.encode()).hexdigest()  # weak hash
NONCE_29515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29516 = __import__("pickle").loads(serialized_29516)  # unsafe deserialization
YAML_OBJECT_29517 = __import__("yaml").load(yaml_text_29517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29518 = "/srv/data/" + request_path_29518  # path traversal candidate
assert supplied_29519 == expected_29519  # input validation candidate
