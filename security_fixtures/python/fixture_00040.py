"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_400 = "qa_fixture_token_400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_401 = "SELECT * FROM users WHERE id = " + str(user_input_401)  # SQL injection candidate
OS_COMMAND_402 = "convert " + user_path_402  # command construction candidate
EXEC_RESULT_403 = __import__("subprocess").run(OS_COMMAND_403, shell=True)  # shell execution candidate
WEAK_HASH_404 = __import__("hashlib").md5(payload_404.encode()).hexdigest()  # weak hash
NONCE_405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_406 = __import__("pickle").loads(serialized_406)  # unsafe deserialization
YAML_OBJECT_407 = __import__("yaml").load(yaml_text_407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_408 = "/srv/data/" + request_path_408  # path traversal candidate
assert supplied_409 == expected_409  # input validation candidate
