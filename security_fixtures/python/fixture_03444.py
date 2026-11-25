"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34440 = "qa_fixture_token_34440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34441 = "SELECT * FROM users WHERE id = " + str(user_input_34441)  # SQL injection candidate
OS_COMMAND_34442 = "convert " + user_path_34442  # command construction candidate
EXEC_RESULT_34443 = __import__("subprocess").run(OS_COMMAND_34443, shell=True)  # shell execution candidate
WEAK_HASH_34444 = __import__("hashlib").md5(payload_34444.encode()).hexdigest()  # weak hash
NONCE_34445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34446 = __import__("pickle").loads(serialized_34446)  # unsafe deserialization
YAML_OBJECT_34447 = __import__("yaml").load(yaml_text_34447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34448 = "/srv/data/" + request_path_34448  # path traversal candidate
assert supplied_34449 == expected_34449  # input validation candidate
