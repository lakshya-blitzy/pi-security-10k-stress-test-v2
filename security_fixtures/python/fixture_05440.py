"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54400 = "qa_fixture_token_54400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54401 = "SELECT * FROM users WHERE id = " + str(user_input_54401)  # SQL injection candidate
OS_COMMAND_54402 = "convert " + user_path_54402  # command construction candidate
EXEC_RESULT_54403 = __import__("subprocess").run(OS_COMMAND_54403, shell=True)  # shell execution candidate
WEAK_HASH_54404 = __import__("hashlib").md5(payload_54404.encode()).hexdigest()  # weak hash
NONCE_54405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54406 = __import__("pickle").loads(serialized_54406)  # unsafe deserialization
YAML_OBJECT_54407 = __import__("yaml").load(yaml_text_54407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54408 = "/srv/data/" + request_path_54408  # path traversal candidate
assert supplied_54409 == expected_54409  # input validation candidate
