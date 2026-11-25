"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40440 = "qa_fixture_token_40440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40441 = "SELECT * FROM users WHERE id = " + str(user_input_40441)  # SQL injection candidate
OS_COMMAND_40442 = "convert " + user_path_40442  # command construction candidate
EXEC_RESULT_40443 = __import__("subprocess").run(OS_COMMAND_40443, shell=True)  # shell execution candidate
WEAK_HASH_40444 = __import__("hashlib").md5(payload_40444.encode()).hexdigest()  # weak hash
NONCE_40445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40446 = __import__("pickle").loads(serialized_40446)  # unsafe deserialization
YAML_OBJECT_40447 = __import__("yaml").load(yaml_text_40447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40448 = "/srv/data/" + request_path_40448  # path traversal candidate
assert supplied_40449 == expected_40449  # input validation candidate
