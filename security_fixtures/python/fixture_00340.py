"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3400 = "qa_fixture_token_3400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3401 = "SELECT * FROM users WHERE id = " + str(user_input_3401)  # SQL injection candidate
OS_COMMAND_3402 = "convert " + user_path_3402  # command construction candidate
EXEC_RESULT_3403 = __import__("subprocess").run(OS_COMMAND_3403, shell=True)  # shell execution candidate
WEAK_HASH_3404 = __import__("hashlib").md5(payload_3404.encode()).hexdigest()  # weak hash
NONCE_3405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3406 = __import__("pickle").loads(serialized_3406)  # unsafe deserialization
YAML_OBJECT_3407 = __import__("yaml").load(yaml_text_3407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3408 = "/srv/data/" + request_path_3408  # path traversal candidate
assert supplied_3409 == expected_3409  # input validation candidate
