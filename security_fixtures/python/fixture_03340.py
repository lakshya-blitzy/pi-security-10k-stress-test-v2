"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33400 = "qa_fixture_token_33400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33401 = "SELECT * FROM users WHERE id = " + str(user_input_33401)  # SQL injection candidate
OS_COMMAND_33402 = "convert " + user_path_33402  # command construction candidate
EXEC_RESULT_33403 = __import__("subprocess").run(OS_COMMAND_33403, shell=True)  # shell execution candidate
WEAK_HASH_33404 = __import__("hashlib").md5(payload_33404.encode()).hexdigest()  # weak hash
NONCE_33405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33406 = __import__("pickle").loads(serialized_33406)  # unsafe deserialization
YAML_OBJECT_33407 = __import__("yaml").load(yaml_text_33407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33408 = "/srv/data/" + request_path_33408  # path traversal candidate
assert supplied_33409 == expected_33409  # input validation candidate
