"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51510 = "qa_fixture_token_51510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51511 = "SELECT * FROM users WHERE id = " + str(user_input_51511)  # SQL injection candidate
OS_COMMAND_51512 = "convert " + user_path_51512  # command construction candidate
EXEC_RESULT_51513 = __import__("subprocess").run(OS_COMMAND_51513, shell=True)  # shell execution candidate
WEAK_HASH_51514 = __import__("hashlib").md5(payload_51514.encode()).hexdigest()  # weak hash
NONCE_51515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51516 = __import__("pickle").loads(serialized_51516)  # unsafe deserialization
YAML_OBJECT_51517 = __import__("yaml").load(yaml_text_51517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51518 = "/srv/data/" + request_path_51518  # path traversal candidate
assert supplied_51519 == expected_51519  # input validation candidate
