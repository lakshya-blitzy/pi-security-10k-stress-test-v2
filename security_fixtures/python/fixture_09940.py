"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99400 = "qa_fixture_token_99400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99401 = "SELECT * FROM users WHERE id = " + str(user_input_99401)  # SQL injection candidate
OS_COMMAND_99402 = "convert " + user_path_99402  # command construction candidate
EXEC_RESULT_99403 = __import__("subprocess").run(OS_COMMAND_99403, shell=True)  # shell execution candidate
WEAK_HASH_99404 = __import__("hashlib").md5(payload_99404.encode()).hexdigest()  # weak hash
NONCE_99405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99406 = __import__("pickle").loads(serialized_99406)  # unsafe deserialization
YAML_OBJECT_99407 = __import__("yaml").load(yaml_text_99407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99408 = "/srv/data/" + request_path_99408  # path traversal candidate
assert supplied_99409 == expected_99409  # input validation candidate
