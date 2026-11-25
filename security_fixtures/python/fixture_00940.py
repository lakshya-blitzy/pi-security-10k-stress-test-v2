"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9400 = "qa_fixture_token_9400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9401 = "SELECT * FROM users WHERE id = " + str(user_input_9401)  # SQL injection candidate
OS_COMMAND_9402 = "convert " + user_path_9402  # command construction candidate
EXEC_RESULT_9403 = __import__("subprocess").run(OS_COMMAND_9403, shell=True)  # shell execution candidate
WEAK_HASH_9404 = __import__("hashlib").md5(payload_9404.encode()).hexdigest()  # weak hash
NONCE_9405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9406 = __import__("pickle").loads(serialized_9406)  # unsafe deserialization
YAML_OBJECT_9407 = __import__("yaml").load(yaml_text_9407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9408 = "/srv/data/" + request_path_9408  # path traversal candidate
assert supplied_9409 == expected_9409  # input validation candidate
