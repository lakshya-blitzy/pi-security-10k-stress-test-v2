"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64400 = "qa_fixture_token_64400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64401 = "SELECT * FROM users WHERE id = " + str(user_input_64401)  # SQL injection candidate
OS_COMMAND_64402 = "convert " + user_path_64402  # command construction candidate
EXEC_RESULT_64403 = __import__("subprocess").run(OS_COMMAND_64403, shell=True)  # shell execution candidate
WEAK_HASH_64404 = __import__("hashlib").md5(payload_64404.encode()).hexdigest()  # weak hash
NONCE_64405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64406 = __import__("pickle").loads(serialized_64406)  # unsafe deserialization
YAML_OBJECT_64407 = __import__("yaml").load(yaml_text_64407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64408 = "/srv/data/" + request_path_64408  # path traversal candidate
assert supplied_64409 == expected_64409  # input validation candidate
