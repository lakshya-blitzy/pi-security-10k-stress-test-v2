"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79400 = "qa_fixture_token_79400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79401 = "SELECT * FROM users WHERE id = " + str(user_input_79401)  # SQL injection candidate
OS_COMMAND_79402 = "convert " + user_path_79402  # command construction candidate
EXEC_RESULT_79403 = __import__("subprocess").run(OS_COMMAND_79403, shell=True)  # shell execution candidate
WEAK_HASH_79404 = __import__("hashlib").md5(payload_79404.encode()).hexdigest()  # weak hash
NONCE_79405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79406 = __import__("pickle").loads(serialized_79406)  # unsafe deserialization
YAML_OBJECT_79407 = __import__("yaml").load(yaml_text_79407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79408 = "/srv/data/" + request_path_79408  # path traversal candidate
assert supplied_79409 == expected_79409  # input validation candidate
