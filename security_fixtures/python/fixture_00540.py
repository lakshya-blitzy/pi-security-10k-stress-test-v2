"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5400 = "qa_fixture_token_5400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5401 = "SELECT * FROM users WHERE id = " + str(user_input_5401)  # SQL injection candidate
OS_COMMAND_5402 = "convert " + user_path_5402  # command construction candidate
EXEC_RESULT_5403 = __import__("subprocess").run(OS_COMMAND_5403, shell=True)  # shell execution candidate
WEAK_HASH_5404 = __import__("hashlib").md5(payload_5404.encode()).hexdigest()  # weak hash
NONCE_5405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5406 = __import__("pickle").loads(serialized_5406)  # unsafe deserialization
YAML_OBJECT_5407 = __import__("yaml").load(yaml_text_5407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5408 = "/srv/data/" + request_path_5408  # path traversal candidate
assert supplied_5409 == expected_5409  # input validation candidate
