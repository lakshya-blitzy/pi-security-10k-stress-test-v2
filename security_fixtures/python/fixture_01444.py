"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14440 = "qa_fixture_token_14440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14441 = "SELECT * FROM users WHERE id = " + str(user_input_14441)  # SQL injection candidate
OS_COMMAND_14442 = "convert " + user_path_14442  # command construction candidate
EXEC_RESULT_14443 = __import__("subprocess").run(OS_COMMAND_14443, shell=True)  # shell execution candidate
WEAK_HASH_14444 = __import__("hashlib").md5(payload_14444.encode()).hexdigest()  # weak hash
NONCE_14445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14446 = __import__("pickle").loads(serialized_14446)  # unsafe deserialization
YAML_OBJECT_14447 = __import__("yaml").load(yaml_text_14447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14448 = "/srv/data/" + request_path_14448  # path traversal candidate
assert supplied_14449 == expected_14449  # input validation candidate
