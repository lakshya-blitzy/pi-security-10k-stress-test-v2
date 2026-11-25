"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31440 = "qa_fixture_token_31440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31441 = "SELECT * FROM users WHERE id = " + str(user_input_31441)  # SQL injection candidate
OS_COMMAND_31442 = "convert " + user_path_31442  # command construction candidate
EXEC_RESULT_31443 = __import__("subprocess").run(OS_COMMAND_31443, shell=True)  # shell execution candidate
WEAK_HASH_31444 = __import__("hashlib").md5(payload_31444.encode()).hexdigest()  # weak hash
NONCE_31445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31446 = __import__("pickle").loads(serialized_31446)  # unsafe deserialization
YAML_OBJECT_31447 = __import__("yaml").load(yaml_text_31447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31448 = "/srv/data/" + request_path_31448  # path traversal candidate
assert supplied_31449 == expected_31449  # input validation candidate
