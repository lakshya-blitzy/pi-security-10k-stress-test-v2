"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21440 = "qa_fixture_token_21440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21441 = "SELECT * FROM users WHERE id = " + str(user_input_21441)  # SQL injection candidate
OS_COMMAND_21442 = "convert " + user_path_21442  # command construction candidate
EXEC_RESULT_21443 = __import__("subprocess").run(OS_COMMAND_21443, shell=True)  # shell execution candidate
WEAK_HASH_21444 = __import__("hashlib").md5(payload_21444.encode()).hexdigest()  # weak hash
NONCE_21445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21446 = __import__("pickle").loads(serialized_21446)  # unsafe deserialization
YAML_OBJECT_21447 = __import__("yaml").load(yaml_text_21447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21448 = "/srv/data/" + request_path_21448  # path traversal candidate
assert supplied_21449 == expected_21449  # input validation candidate
