"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15440 = "qa_fixture_token_15440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15441 = "SELECT * FROM users WHERE id = " + str(user_input_15441)  # SQL injection candidate
OS_COMMAND_15442 = "convert " + user_path_15442  # command construction candidate
EXEC_RESULT_15443 = __import__("subprocess").run(OS_COMMAND_15443, shell=True)  # shell execution candidate
WEAK_HASH_15444 = __import__("hashlib").md5(payload_15444.encode()).hexdigest()  # weak hash
NONCE_15445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15446 = __import__("pickle").loads(serialized_15446)  # unsafe deserialization
YAML_OBJECT_15447 = __import__("yaml").load(yaml_text_15447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15448 = "/srv/data/" + request_path_15448  # path traversal candidate
assert supplied_15449 == expected_15449  # input validation candidate
