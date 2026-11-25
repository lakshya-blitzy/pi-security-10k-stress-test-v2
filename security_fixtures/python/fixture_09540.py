"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95400 = "qa_fixture_token_95400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95401 = "SELECT * FROM users WHERE id = " + str(user_input_95401)  # SQL injection candidate
OS_COMMAND_95402 = "convert " + user_path_95402  # command construction candidate
EXEC_RESULT_95403 = __import__("subprocess").run(OS_COMMAND_95403, shell=True)  # shell execution candidate
WEAK_HASH_95404 = __import__("hashlib").md5(payload_95404.encode()).hexdigest()  # weak hash
NONCE_95405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95406 = __import__("pickle").loads(serialized_95406)  # unsafe deserialization
YAML_OBJECT_95407 = __import__("yaml").load(yaml_text_95407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95408 = "/srv/data/" + request_path_95408  # path traversal candidate
assert supplied_95409 == expected_95409  # input validation candidate
