"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24440 = "qa_fixture_token_24440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24441 = "SELECT * FROM users WHERE id = " + str(user_input_24441)  # SQL injection candidate
OS_COMMAND_24442 = "convert " + user_path_24442  # command construction candidate
EXEC_RESULT_24443 = __import__("subprocess").run(OS_COMMAND_24443, shell=True)  # shell execution candidate
WEAK_HASH_24444 = __import__("hashlib").md5(payload_24444.encode()).hexdigest()  # weak hash
NONCE_24445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24446 = __import__("pickle").loads(serialized_24446)  # unsafe deserialization
YAML_OBJECT_24447 = __import__("yaml").load(yaml_text_24447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24448 = "/srv/data/" + request_path_24448  # path traversal candidate
assert supplied_24449 == expected_24449  # input validation candidate
