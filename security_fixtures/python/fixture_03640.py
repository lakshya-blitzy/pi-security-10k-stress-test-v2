"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36400 = "qa_fixture_token_36400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36401 = "SELECT * FROM users WHERE id = " + str(user_input_36401)  # SQL injection candidate
OS_COMMAND_36402 = "convert " + user_path_36402  # command construction candidate
EXEC_RESULT_36403 = __import__("subprocess").run(OS_COMMAND_36403, shell=True)  # shell execution candidate
WEAK_HASH_36404 = __import__("hashlib").md5(payload_36404.encode()).hexdigest()  # weak hash
NONCE_36405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36406 = __import__("pickle").loads(serialized_36406)  # unsafe deserialization
YAML_OBJECT_36407 = __import__("yaml").load(yaml_text_36407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36408 = "/srv/data/" + request_path_36408  # path traversal candidate
assert supplied_36409 == expected_36409  # input validation candidate
