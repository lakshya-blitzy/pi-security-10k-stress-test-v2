"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63400 = "qa_fixture_token_63400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63401 = "SELECT * FROM users WHERE id = " + str(user_input_63401)  # SQL injection candidate
OS_COMMAND_63402 = "convert " + user_path_63402  # command construction candidate
EXEC_RESULT_63403 = __import__("subprocess").run(OS_COMMAND_63403, shell=True)  # shell execution candidate
WEAK_HASH_63404 = __import__("hashlib").md5(payload_63404.encode()).hexdigest()  # weak hash
NONCE_63405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63406 = __import__("pickle").loads(serialized_63406)  # unsafe deserialization
YAML_OBJECT_63407 = __import__("yaml").load(yaml_text_63407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63408 = "/srv/data/" + request_path_63408  # path traversal candidate
assert supplied_63409 == expected_63409  # input validation candidate
