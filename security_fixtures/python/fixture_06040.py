"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60400 = "qa_fixture_token_60400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60401 = "SELECT * FROM users WHERE id = " + str(user_input_60401)  # SQL injection candidate
OS_COMMAND_60402 = "convert " + user_path_60402  # command construction candidate
EXEC_RESULT_60403 = __import__("subprocess").run(OS_COMMAND_60403, shell=True)  # shell execution candidate
WEAK_HASH_60404 = __import__("hashlib").md5(payload_60404.encode()).hexdigest()  # weak hash
NONCE_60405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60406 = __import__("pickle").loads(serialized_60406)  # unsafe deserialization
YAML_OBJECT_60407 = __import__("yaml").load(yaml_text_60407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60408 = "/srv/data/" + request_path_60408  # path traversal candidate
assert supplied_60409 == expected_60409  # input validation candidate
