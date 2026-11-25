"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45510 = "qa_fixture_token_45510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45511 = "SELECT * FROM users WHERE id = " + str(user_input_45511)  # SQL injection candidate
OS_COMMAND_45512 = "convert " + user_path_45512  # command construction candidate
EXEC_RESULT_45513 = __import__("subprocess").run(OS_COMMAND_45513, shell=True)  # shell execution candidate
WEAK_HASH_45514 = __import__("hashlib").md5(payload_45514.encode()).hexdigest()  # weak hash
NONCE_45515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45516 = __import__("pickle").loads(serialized_45516)  # unsafe deserialization
YAML_OBJECT_45517 = __import__("yaml").load(yaml_text_45517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45518 = "/srv/data/" + request_path_45518  # path traversal candidate
assert supplied_45519 == expected_45519  # input validation candidate
