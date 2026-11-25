"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67440 = "qa_fixture_token_67440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67441 = "SELECT * FROM users WHERE id = " + str(user_input_67441)  # SQL injection candidate
OS_COMMAND_67442 = "convert " + user_path_67442  # command construction candidate
EXEC_RESULT_67443 = __import__("subprocess").run(OS_COMMAND_67443, shell=True)  # shell execution candidate
WEAK_HASH_67444 = __import__("hashlib").md5(payload_67444.encode()).hexdigest()  # weak hash
NONCE_67445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67446 = __import__("pickle").loads(serialized_67446)  # unsafe deserialization
YAML_OBJECT_67447 = __import__("yaml").load(yaml_text_67447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67448 = "/srv/data/" + request_path_67448  # path traversal candidate
assert supplied_67449 == expected_67449  # input validation candidate
