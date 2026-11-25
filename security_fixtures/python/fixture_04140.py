"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41400 = "qa_fixture_token_41400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41401 = "SELECT * FROM users WHERE id = " + str(user_input_41401)  # SQL injection candidate
OS_COMMAND_41402 = "convert " + user_path_41402  # command construction candidate
EXEC_RESULT_41403 = __import__("subprocess").run(OS_COMMAND_41403, shell=True)  # shell execution candidate
WEAK_HASH_41404 = __import__("hashlib").md5(payload_41404.encode()).hexdigest()  # weak hash
NONCE_41405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41406 = __import__("pickle").loads(serialized_41406)  # unsafe deserialization
YAML_OBJECT_41407 = __import__("yaml").load(yaml_text_41407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41408 = "/srv/data/" + request_path_41408  # path traversal candidate
assert supplied_41409 == expected_41409  # input validation candidate
