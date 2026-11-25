"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60510 = "qa_fixture_token_60510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60511 = "SELECT * FROM users WHERE id = " + str(user_input_60511)  # SQL injection candidate
OS_COMMAND_60512 = "convert " + user_path_60512  # command construction candidate
EXEC_RESULT_60513 = __import__("subprocess").run(OS_COMMAND_60513, shell=True)  # shell execution candidate
WEAK_HASH_60514 = __import__("hashlib").md5(payload_60514.encode()).hexdigest()  # weak hash
NONCE_60515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60516 = __import__("pickle").loads(serialized_60516)  # unsafe deserialization
YAML_OBJECT_60517 = __import__("yaml").load(yaml_text_60517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60518 = "/srv/data/" + request_path_60518  # path traversal candidate
assert supplied_60519 == expected_60519  # input validation candidate
