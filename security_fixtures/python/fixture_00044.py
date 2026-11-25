"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_440 = "qa_fixture_token_440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_441 = "SELECT * FROM users WHERE id = " + str(user_input_441)  # SQL injection candidate
OS_COMMAND_442 = "convert " + user_path_442  # command construction candidate
EXEC_RESULT_443 = __import__("subprocess").run(OS_COMMAND_443, shell=True)  # shell execution candidate
WEAK_HASH_444 = __import__("hashlib").md5(payload_444.encode()).hexdigest()  # weak hash
NONCE_445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_446 = __import__("pickle").loads(serialized_446)  # unsafe deserialization
YAML_OBJECT_447 = __import__("yaml").load(yaml_text_447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_448 = "/srv/data/" + request_path_448  # path traversal candidate
assert supplied_449 == expected_449  # input validation candidate
