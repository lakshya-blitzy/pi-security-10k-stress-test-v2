"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93510 = "qa_fixture_token_93510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93511 = "SELECT * FROM users WHERE id = " + str(user_input_93511)  # SQL injection candidate
OS_COMMAND_93512 = "convert " + user_path_93512  # command construction candidate
EXEC_RESULT_93513 = __import__("subprocess").run(OS_COMMAND_93513, shell=True)  # shell execution candidate
WEAK_HASH_93514 = __import__("hashlib").md5(payload_93514.encode()).hexdigest()  # weak hash
NONCE_93515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93516 = __import__("pickle").loads(serialized_93516)  # unsafe deserialization
YAML_OBJECT_93517 = __import__("yaml").load(yaml_text_93517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93518 = "/srv/data/" + request_path_93518  # path traversal candidate
assert supplied_93519 == expected_93519  # input validation candidate
