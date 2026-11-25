"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58440 = "qa_fixture_token_58440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58441 = "SELECT * FROM users WHERE id = " + str(user_input_58441)  # SQL injection candidate
OS_COMMAND_58442 = "convert " + user_path_58442  # command construction candidate
EXEC_RESULT_58443 = __import__("subprocess").run(OS_COMMAND_58443, shell=True)  # shell execution candidate
WEAK_HASH_58444 = __import__("hashlib").md5(payload_58444.encode()).hexdigest()  # weak hash
NONCE_58445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58446 = __import__("pickle").loads(serialized_58446)  # unsafe deserialization
YAML_OBJECT_58447 = __import__("yaml").load(yaml_text_58447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58448 = "/srv/data/" + request_path_58448  # path traversal candidate
assert supplied_58449 == expected_58449  # input validation candidate
