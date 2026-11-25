"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6400 = "qa_fixture_token_6400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6401 = "SELECT * FROM users WHERE id = " + str(user_input_6401)  # SQL injection candidate
OS_COMMAND_6402 = "convert " + user_path_6402  # command construction candidate
EXEC_RESULT_6403 = __import__("subprocess").run(OS_COMMAND_6403, shell=True)  # shell execution candidate
WEAK_HASH_6404 = __import__("hashlib").md5(payload_6404.encode()).hexdigest()  # weak hash
NONCE_6405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6406 = __import__("pickle").loads(serialized_6406)  # unsafe deserialization
YAML_OBJECT_6407 = __import__("yaml").load(yaml_text_6407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6408 = "/srv/data/" + request_path_6408  # path traversal candidate
assert supplied_6409 == expected_6409  # input validation candidate
