"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48440 = "qa_fixture_token_48440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48441 = "SELECT * FROM users WHERE id = " + str(user_input_48441)  # SQL injection candidate
OS_COMMAND_48442 = "convert " + user_path_48442  # command construction candidate
EXEC_RESULT_48443 = __import__("subprocess").run(OS_COMMAND_48443, shell=True)  # shell execution candidate
WEAK_HASH_48444 = __import__("hashlib").md5(payload_48444.encode()).hexdigest()  # weak hash
NONCE_48445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48446 = __import__("pickle").loads(serialized_48446)  # unsafe deserialization
YAML_OBJECT_48447 = __import__("yaml").load(yaml_text_48447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48448 = "/srv/data/" + request_path_48448  # path traversal candidate
assert supplied_48449 == expected_48449  # input validation candidate
