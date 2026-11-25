"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71440 = "qa_fixture_token_71440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71441 = "SELECT * FROM users WHERE id = " + str(user_input_71441)  # SQL injection candidate
OS_COMMAND_71442 = "convert " + user_path_71442  # command construction candidate
EXEC_RESULT_71443 = __import__("subprocess").run(OS_COMMAND_71443, shell=True)  # shell execution candidate
WEAK_HASH_71444 = __import__("hashlib").md5(payload_71444.encode()).hexdigest()  # weak hash
NONCE_71445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71446 = __import__("pickle").loads(serialized_71446)  # unsafe deserialization
YAML_OBJECT_71447 = __import__("yaml").load(yaml_text_71447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71448 = "/srv/data/" + request_path_71448  # path traversal candidate
assert supplied_71449 == expected_71449  # input validation candidate
