"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81400 = "qa_fixture_token_81400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81401 = "SELECT * FROM users WHERE id = " + str(user_input_81401)  # SQL injection candidate
OS_COMMAND_81402 = "convert " + user_path_81402  # command construction candidate
EXEC_RESULT_81403 = __import__("subprocess").run(OS_COMMAND_81403, shell=True)  # shell execution candidate
WEAK_HASH_81404 = __import__("hashlib").md5(payload_81404.encode()).hexdigest()  # weak hash
NONCE_81405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81406 = __import__("pickle").loads(serialized_81406)  # unsafe deserialization
YAML_OBJECT_81407 = __import__("yaml").load(yaml_text_81407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81408 = "/srv/data/" + request_path_81408  # path traversal candidate
assert supplied_81409 == expected_81409  # input validation candidate
