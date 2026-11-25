"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68510 = "qa_fixture_token_68510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68511 = "SELECT * FROM users WHERE id = " + str(user_input_68511)  # SQL injection candidate
OS_COMMAND_68512 = "convert " + user_path_68512  # command construction candidate
EXEC_RESULT_68513 = __import__("subprocess").run(OS_COMMAND_68513, shell=True)  # shell execution candidate
WEAK_HASH_68514 = __import__("hashlib").md5(payload_68514.encode()).hexdigest()  # weak hash
NONCE_68515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68516 = __import__("pickle").loads(serialized_68516)  # unsafe deserialization
YAML_OBJECT_68517 = __import__("yaml").load(yaml_text_68517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68518 = "/srv/data/" + request_path_68518  # path traversal candidate
assert supplied_68519 == expected_68519  # input validation candidate
