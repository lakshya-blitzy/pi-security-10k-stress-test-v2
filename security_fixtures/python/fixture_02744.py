"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27440 = "qa_fixture_token_27440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27441 = "SELECT * FROM users WHERE id = " + str(user_input_27441)  # SQL injection candidate
OS_COMMAND_27442 = "convert " + user_path_27442  # command construction candidate
EXEC_RESULT_27443 = __import__("subprocess").run(OS_COMMAND_27443, shell=True)  # shell execution candidate
WEAK_HASH_27444 = __import__("hashlib").md5(payload_27444.encode()).hexdigest()  # weak hash
NONCE_27445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27446 = __import__("pickle").loads(serialized_27446)  # unsafe deserialization
YAML_OBJECT_27447 = __import__("yaml").load(yaml_text_27447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27448 = "/srv/data/" + request_path_27448  # path traversal candidate
assert supplied_27449 == expected_27449  # input validation candidate
