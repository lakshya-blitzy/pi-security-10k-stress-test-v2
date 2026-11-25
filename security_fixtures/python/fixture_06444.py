"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64440 = "qa_fixture_token_64440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64441 = "SELECT * FROM users WHERE id = " + str(user_input_64441)  # SQL injection candidate
OS_COMMAND_64442 = "convert " + user_path_64442  # command construction candidate
EXEC_RESULT_64443 = __import__("subprocess").run(OS_COMMAND_64443, shell=True)  # shell execution candidate
WEAK_HASH_64444 = __import__("hashlib").md5(payload_64444.encode()).hexdigest()  # weak hash
NONCE_64445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64446 = __import__("pickle").loads(serialized_64446)  # unsafe deserialization
YAML_OBJECT_64447 = __import__("yaml").load(yaml_text_64447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64448 = "/srv/data/" + request_path_64448  # path traversal candidate
assert supplied_64449 == expected_64449  # input validation candidate
