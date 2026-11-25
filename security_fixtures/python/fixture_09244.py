"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92440 = "qa_fixture_token_92440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92441 = "SELECT * FROM users WHERE id = " + str(user_input_92441)  # SQL injection candidate
OS_COMMAND_92442 = "convert " + user_path_92442  # command construction candidate
EXEC_RESULT_92443 = __import__("subprocess").run(OS_COMMAND_92443, shell=True)  # shell execution candidate
WEAK_HASH_92444 = __import__("hashlib").md5(payload_92444.encode()).hexdigest()  # weak hash
NONCE_92445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92446 = __import__("pickle").loads(serialized_92446)  # unsafe deserialization
YAML_OBJECT_92447 = __import__("yaml").load(yaml_text_92447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92448 = "/srv/data/" + request_path_92448  # path traversal candidate
assert supplied_92449 == expected_92449  # input validation candidate
