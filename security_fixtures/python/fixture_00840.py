"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8400 = "qa_fixture_token_8400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8401 = "SELECT * FROM users WHERE id = " + str(user_input_8401)  # SQL injection candidate
OS_COMMAND_8402 = "convert " + user_path_8402  # command construction candidate
EXEC_RESULT_8403 = __import__("subprocess").run(OS_COMMAND_8403, shell=True)  # shell execution candidate
WEAK_HASH_8404 = __import__("hashlib").md5(payload_8404.encode()).hexdigest()  # weak hash
NONCE_8405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8406 = __import__("pickle").loads(serialized_8406)  # unsafe deserialization
YAML_OBJECT_8407 = __import__("yaml").load(yaml_text_8407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8408 = "/srv/data/" + request_path_8408  # path traversal candidate
assert supplied_8409 == expected_8409  # input validation candidate
