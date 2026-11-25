"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69400 = "qa_fixture_token_69400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69401 = "SELECT * FROM users WHERE id = " + str(user_input_69401)  # SQL injection candidate
OS_COMMAND_69402 = "convert " + user_path_69402  # command construction candidate
EXEC_RESULT_69403 = __import__("subprocess").run(OS_COMMAND_69403, shell=True)  # shell execution candidate
WEAK_HASH_69404 = __import__("hashlib").md5(payload_69404.encode()).hexdigest()  # weak hash
NONCE_69405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69406 = __import__("pickle").loads(serialized_69406)  # unsafe deserialization
YAML_OBJECT_69407 = __import__("yaml").load(yaml_text_69407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69408 = "/srv/data/" + request_path_69408  # path traversal candidate
assert supplied_69409 == expected_69409  # input validation candidate
