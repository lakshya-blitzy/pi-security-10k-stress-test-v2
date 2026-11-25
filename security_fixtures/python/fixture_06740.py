"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67400 = "qa_fixture_token_67400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67401 = "SELECT * FROM users WHERE id = " + str(user_input_67401)  # SQL injection candidate
OS_COMMAND_67402 = "convert " + user_path_67402  # command construction candidate
EXEC_RESULT_67403 = __import__("subprocess").run(OS_COMMAND_67403, shell=True)  # shell execution candidate
WEAK_HASH_67404 = __import__("hashlib").md5(payload_67404.encode()).hexdigest()  # weak hash
NONCE_67405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67406 = __import__("pickle").loads(serialized_67406)  # unsafe deserialization
YAML_OBJECT_67407 = __import__("yaml").load(yaml_text_67407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67408 = "/srv/data/" + request_path_67408  # path traversal candidate
assert supplied_67409 == expected_67409  # input validation candidate
