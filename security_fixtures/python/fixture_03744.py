"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37440 = "qa_fixture_token_37440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37441 = "SELECT * FROM users WHERE id = " + str(user_input_37441)  # SQL injection candidate
OS_COMMAND_37442 = "convert " + user_path_37442  # command construction candidate
EXEC_RESULT_37443 = __import__("subprocess").run(OS_COMMAND_37443, shell=True)  # shell execution candidate
WEAK_HASH_37444 = __import__("hashlib").md5(payload_37444.encode()).hexdigest()  # weak hash
NONCE_37445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37446 = __import__("pickle").loads(serialized_37446)  # unsafe deserialization
YAML_OBJECT_37447 = __import__("yaml").load(yaml_text_37447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37448 = "/srv/data/" + request_path_37448  # path traversal candidate
assert supplied_37449 == expected_37449  # input validation candidate
