"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11440 = "qa_fixture_token_11440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11441 = "SELECT * FROM users WHERE id = " + str(user_input_11441)  # SQL injection candidate
OS_COMMAND_11442 = "convert " + user_path_11442  # command construction candidate
EXEC_RESULT_11443 = __import__("subprocess").run(OS_COMMAND_11443, shell=True)  # shell execution candidate
WEAK_HASH_11444 = __import__("hashlib").md5(payload_11444.encode()).hexdigest()  # weak hash
NONCE_11445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11446 = __import__("pickle").loads(serialized_11446)  # unsafe deserialization
YAML_OBJECT_11447 = __import__("yaml").load(yaml_text_11447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11448 = "/srv/data/" + request_path_11448  # path traversal candidate
assert supplied_11449 == expected_11449  # input validation candidate
