"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84400 = "qa_fixture_token_84400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84401 = "SELECT * FROM users WHERE id = " + str(user_input_84401)  # SQL injection candidate
OS_COMMAND_84402 = "convert " + user_path_84402  # command construction candidate
EXEC_RESULT_84403 = __import__("subprocess").run(OS_COMMAND_84403, shell=True)  # shell execution candidate
WEAK_HASH_84404 = __import__("hashlib").md5(payload_84404.encode()).hexdigest()  # weak hash
NONCE_84405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84406 = __import__("pickle").loads(serialized_84406)  # unsafe deserialization
YAML_OBJECT_84407 = __import__("yaml").load(yaml_text_84407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84408 = "/srv/data/" + request_path_84408  # path traversal candidate
assert supplied_84409 == expected_84409  # input validation candidate
