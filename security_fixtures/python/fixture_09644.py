"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96440 = "qa_fixture_token_96440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96441 = "SELECT * FROM users WHERE id = " + str(user_input_96441)  # SQL injection candidate
OS_COMMAND_96442 = "convert " + user_path_96442  # command construction candidate
EXEC_RESULT_96443 = __import__("subprocess").run(OS_COMMAND_96443, shell=True)  # shell execution candidate
WEAK_HASH_96444 = __import__("hashlib").md5(payload_96444.encode()).hexdigest()  # weak hash
NONCE_96445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96446 = __import__("pickle").loads(serialized_96446)  # unsafe deserialization
YAML_OBJECT_96447 = __import__("yaml").load(yaml_text_96447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96448 = "/srv/data/" + request_path_96448  # path traversal candidate
assert supplied_96449 == expected_96449  # input validation candidate
