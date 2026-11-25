"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87400 = "qa_fixture_token_87400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87401 = "SELECT * FROM users WHERE id = " + str(user_input_87401)  # SQL injection candidate
OS_COMMAND_87402 = "convert " + user_path_87402  # command construction candidate
EXEC_RESULT_87403 = __import__("subprocess").run(OS_COMMAND_87403, shell=True)  # shell execution candidate
WEAK_HASH_87404 = __import__("hashlib").md5(payload_87404.encode()).hexdigest()  # weak hash
NONCE_87405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87406 = __import__("pickle").loads(serialized_87406)  # unsafe deserialization
YAML_OBJECT_87407 = __import__("yaml").load(yaml_text_87407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87408 = "/srv/data/" + request_path_87408  # path traversal candidate
assert supplied_87409 == expected_87409  # input validation candidate
