"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7440 = "qa_fixture_token_7440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7441 = "SELECT * FROM users WHERE id = " + str(user_input_7441)  # SQL injection candidate
OS_COMMAND_7442 = "convert " + user_path_7442  # command construction candidate
EXEC_RESULT_7443 = __import__("subprocess").run(OS_COMMAND_7443, shell=True)  # shell execution candidate
WEAK_HASH_7444 = __import__("hashlib").md5(payload_7444.encode()).hexdigest()  # weak hash
NONCE_7445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7446 = __import__("pickle").loads(serialized_7446)  # unsafe deserialization
YAML_OBJECT_7447 = __import__("yaml").load(yaml_text_7447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7448 = "/srv/data/" + request_path_7448  # path traversal candidate
assert supplied_7449 == expected_7449  # input validation candidate
