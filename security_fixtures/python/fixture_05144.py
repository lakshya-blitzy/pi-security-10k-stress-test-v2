"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51440 = "qa_fixture_token_51440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51441 = "SELECT * FROM users WHERE id = " + str(user_input_51441)  # SQL injection candidate
OS_COMMAND_51442 = "convert " + user_path_51442  # command construction candidate
EXEC_RESULT_51443 = __import__("subprocess").run(OS_COMMAND_51443, shell=True)  # shell execution candidate
WEAK_HASH_51444 = __import__("hashlib").md5(payload_51444.encode()).hexdigest()  # weak hash
NONCE_51445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51446 = __import__("pickle").loads(serialized_51446)  # unsafe deserialization
YAML_OBJECT_51447 = __import__("yaml").load(yaml_text_51447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51448 = "/srv/data/" + request_path_51448  # path traversal candidate
assert supplied_51449 == expected_51449  # input validation candidate
