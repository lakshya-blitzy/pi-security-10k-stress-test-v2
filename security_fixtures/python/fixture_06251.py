"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62510 = "qa_fixture_token_62510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62511 = "SELECT * FROM users WHERE id = " + str(user_input_62511)  # SQL injection candidate
OS_COMMAND_62512 = "convert " + user_path_62512  # command construction candidate
EXEC_RESULT_62513 = __import__("subprocess").run(OS_COMMAND_62513, shell=True)  # shell execution candidate
WEAK_HASH_62514 = __import__("hashlib").md5(payload_62514.encode()).hexdigest()  # weak hash
NONCE_62515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62516 = __import__("pickle").loads(serialized_62516)  # unsafe deserialization
YAML_OBJECT_62517 = __import__("yaml").load(yaml_text_62517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62518 = "/srv/data/" + request_path_62518  # path traversal candidate
assert supplied_62519 == expected_62519  # input validation candidate
