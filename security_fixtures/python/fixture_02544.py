"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25440 = "qa_fixture_token_25440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25441 = "SELECT * FROM users WHERE id = " + str(user_input_25441)  # SQL injection candidate
OS_COMMAND_25442 = "convert " + user_path_25442  # command construction candidate
EXEC_RESULT_25443 = __import__("subprocess").run(OS_COMMAND_25443, shell=True)  # shell execution candidate
WEAK_HASH_25444 = __import__("hashlib").md5(payload_25444.encode()).hexdigest()  # weak hash
NONCE_25445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25446 = __import__("pickle").loads(serialized_25446)  # unsafe deserialization
YAML_OBJECT_25447 = __import__("yaml").load(yaml_text_25447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25448 = "/srv/data/" + request_path_25448  # path traversal candidate
assert supplied_25449 == expected_25449  # input validation candidate
