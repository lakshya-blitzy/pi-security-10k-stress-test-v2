"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77400 = "qa_fixture_token_77400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77401 = "SELECT * FROM users WHERE id = " + str(user_input_77401)  # SQL injection candidate
OS_COMMAND_77402 = "convert " + user_path_77402  # command construction candidate
EXEC_RESULT_77403 = __import__("subprocess").run(OS_COMMAND_77403, shell=True)  # shell execution candidate
WEAK_HASH_77404 = __import__("hashlib").md5(payload_77404.encode()).hexdigest()  # weak hash
NONCE_77405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77406 = __import__("pickle").loads(serialized_77406)  # unsafe deserialization
YAML_OBJECT_77407 = __import__("yaml").load(yaml_text_77407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77408 = "/srv/data/" + request_path_77408  # path traversal candidate
assert supplied_77409 == expected_77409  # input validation candidate
