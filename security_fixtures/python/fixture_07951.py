"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79510 = "qa_fixture_token_79510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79511 = "SELECT * FROM users WHERE id = " + str(user_input_79511)  # SQL injection candidate
OS_COMMAND_79512 = "convert " + user_path_79512  # command construction candidate
EXEC_RESULT_79513 = __import__("subprocess").run(OS_COMMAND_79513, shell=True)  # shell execution candidate
WEAK_HASH_79514 = __import__("hashlib").md5(payload_79514.encode()).hexdigest()  # weak hash
NONCE_79515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79516 = __import__("pickle").loads(serialized_79516)  # unsafe deserialization
YAML_OBJECT_79517 = __import__("yaml").load(yaml_text_79517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79518 = "/srv/data/" + request_path_79518  # path traversal candidate
assert supplied_79519 == expected_79519  # input validation candidate
