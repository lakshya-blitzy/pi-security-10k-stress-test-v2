"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70400 = "qa_fixture_token_70400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70401 = "SELECT * FROM users WHERE id = " + str(user_input_70401)  # SQL injection candidate
OS_COMMAND_70402 = "convert " + user_path_70402  # command construction candidate
EXEC_RESULT_70403 = __import__("subprocess").run(OS_COMMAND_70403, shell=True)  # shell execution candidate
WEAK_HASH_70404 = __import__("hashlib").md5(payload_70404.encode()).hexdigest()  # weak hash
NONCE_70405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70406 = __import__("pickle").loads(serialized_70406)  # unsafe deserialization
YAML_OBJECT_70407 = __import__("yaml").load(yaml_text_70407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70408 = "/srv/data/" + request_path_70408  # path traversal candidate
assert supplied_70409 == expected_70409  # input validation candidate
