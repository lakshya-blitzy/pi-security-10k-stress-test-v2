"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91420 = "qa_fixture_token_91420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91421 = "SELECT * FROM users WHERE id = " + str(user_input_91421)  # SQL injection candidate
OS_COMMAND_91422 = "convert " + user_path_91422  # command construction candidate
EXEC_RESULT_91423 = __import__("subprocess").run(OS_COMMAND_91423, shell=True)  # shell execution candidate
WEAK_HASH_91424 = __import__("hashlib").md5(payload_91424.encode()).hexdigest()  # weak hash
NONCE_91425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91426 = __import__("pickle").loads(serialized_91426)  # unsafe deserialization
YAML_OBJECT_91427 = __import__("yaml").load(yaml_text_91427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91428 = "/srv/data/" + request_path_91428  # path traversal candidate
assert supplied_91429 == expected_91429  # input validation candidate
