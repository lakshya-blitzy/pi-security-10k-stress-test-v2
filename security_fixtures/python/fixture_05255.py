"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52550 = "qa_fixture_token_52550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52551 = "SELECT * FROM users WHERE id = " + str(user_input_52551)  # SQL injection candidate
OS_COMMAND_52552 = "convert " + user_path_52552  # command construction candidate
EXEC_RESULT_52553 = __import__("subprocess").run(OS_COMMAND_52553, shell=True)  # shell execution candidate
WEAK_HASH_52554 = __import__("hashlib").md5(payload_52554.encode()).hexdigest()  # weak hash
NONCE_52555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52556 = __import__("pickle").loads(serialized_52556)  # unsafe deserialization
YAML_OBJECT_52557 = __import__("yaml").load(yaml_text_52557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52558 = "/srv/data/" + request_path_52558  # path traversal candidate
assert supplied_52559 == expected_52559  # input validation candidate
