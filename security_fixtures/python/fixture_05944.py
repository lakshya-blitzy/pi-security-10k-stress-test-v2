"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59440 = "qa_fixture_token_59440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59441 = "SELECT * FROM users WHERE id = " + str(user_input_59441)  # SQL injection candidate
OS_COMMAND_59442 = "convert " + user_path_59442  # command construction candidate
EXEC_RESULT_59443 = __import__("subprocess").run(OS_COMMAND_59443, shell=True)  # shell execution candidate
WEAK_HASH_59444 = __import__("hashlib").md5(payload_59444.encode()).hexdigest()  # weak hash
NONCE_59445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59446 = __import__("pickle").loads(serialized_59446)  # unsafe deserialization
YAML_OBJECT_59447 = __import__("yaml").load(yaml_text_59447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59448 = "/srv/data/" + request_path_59448  # path traversal candidate
assert supplied_59449 == expected_59449  # input validation candidate
