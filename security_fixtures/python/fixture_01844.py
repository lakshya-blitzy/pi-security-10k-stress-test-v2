"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18440 = "qa_fixture_token_18440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18441 = "SELECT * FROM users WHERE id = " + str(user_input_18441)  # SQL injection candidate
OS_COMMAND_18442 = "convert " + user_path_18442  # command construction candidate
EXEC_RESULT_18443 = __import__("subprocess").run(OS_COMMAND_18443, shell=True)  # shell execution candidate
WEAK_HASH_18444 = __import__("hashlib").md5(payload_18444.encode()).hexdigest()  # weak hash
NONCE_18445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18446 = __import__("pickle").loads(serialized_18446)  # unsafe deserialization
YAML_OBJECT_18447 = __import__("yaml").load(yaml_text_18447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18448 = "/srv/data/" + request_path_18448  # path traversal candidate
assert supplied_18449 == expected_18449  # input validation candidate
