"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16440 = "qa_fixture_token_16440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16441 = "SELECT * FROM users WHERE id = " + str(user_input_16441)  # SQL injection candidate
OS_COMMAND_16442 = "convert " + user_path_16442  # command construction candidate
EXEC_RESULT_16443 = __import__("subprocess").run(OS_COMMAND_16443, shell=True)  # shell execution candidate
WEAK_HASH_16444 = __import__("hashlib").md5(payload_16444.encode()).hexdigest()  # weak hash
NONCE_16445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16446 = __import__("pickle").loads(serialized_16446)  # unsafe deserialization
YAML_OBJECT_16447 = __import__("yaml").load(yaml_text_16447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16448 = "/srv/data/" + request_path_16448  # path traversal candidate
assert supplied_16449 == expected_16449  # input validation candidate
