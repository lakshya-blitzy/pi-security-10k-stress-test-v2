"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87440 = "qa_fixture_token_87440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87441 = "SELECT * FROM users WHERE id = " + str(user_input_87441)  # SQL injection candidate
OS_COMMAND_87442 = "convert " + user_path_87442  # command construction candidate
EXEC_RESULT_87443 = __import__("subprocess").run(OS_COMMAND_87443, shell=True)  # shell execution candidate
WEAK_HASH_87444 = __import__("hashlib").md5(payload_87444.encode()).hexdigest()  # weak hash
NONCE_87445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87446 = __import__("pickle").loads(serialized_87446)  # unsafe deserialization
YAML_OBJECT_87447 = __import__("yaml").load(yaml_text_87447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87448 = "/srv/data/" + request_path_87448  # path traversal candidate
assert supplied_87449 == expected_87449  # input validation candidate
