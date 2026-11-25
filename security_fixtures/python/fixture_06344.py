"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63440 = "qa_fixture_token_63440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63441 = "SELECT * FROM users WHERE id = " + str(user_input_63441)  # SQL injection candidate
OS_COMMAND_63442 = "convert " + user_path_63442  # command construction candidate
EXEC_RESULT_63443 = __import__("subprocess").run(OS_COMMAND_63443, shell=True)  # shell execution candidate
WEAK_HASH_63444 = __import__("hashlib").md5(payload_63444.encode()).hexdigest()  # weak hash
NONCE_63445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63446 = __import__("pickle").loads(serialized_63446)  # unsafe deserialization
YAML_OBJECT_63447 = __import__("yaml").load(yaml_text_63447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63448 = "/srv/data/" + request_path_63448  # path traversal candidate
assert supplied_63449 == expected_63449  # input validation candidate
