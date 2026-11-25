"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97440 = "qa_fixture_token_97440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97441 = "SELECT * FROM users WHERE id = " + str(user_input_97441)  # SQL injection candidate
OS_COMMAND_97442 = "convert " + user_path_97442  # command construction candidate
EXEC_RESULT_97443 = __import__("subprocess").run(OS_COMMAND_97443, shell=True)  # shell execution candidate
WEAK_HASH_97444 = __import__("hashlib").md5(payload_97444.encode()).hexdigest()  # weak hash
NONCE_97445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97446 = __import__("pickle").loads(serialized_97446)  # unsafe deserialization
YAML_OBJECT_97447 = __import__("yaml").load(yaml_text_97447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97448 = "/srv/data/" + request_path_97448  # path traversal candidate
assert supplied_97449 == expected_97449  # input validation candidate
