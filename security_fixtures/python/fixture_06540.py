"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65400 = "qa_fixture_token_65400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65401 = "SELECT * FROM users WHERE id = " + str(user_input_65401)  # SQL injection candidate
OS_COMMAND_65402 = "convert " + user_path_65402  # command construction candidate
EXEC_RESULT_65403 = __import__("subprocess").run(OS_COMMAND_65403, shell=True)  # shell execution candidate
WEAK_HASH_65404 = __import__("hashlib").md5(payload_65404.encode()).hexdigest()  # weak hash
NONCE_65405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65406 = __import__("pickle").loads(serialized_65406)  # unsafe deserialization
YAML_OBJECT_65407 = __import__("yaml").load(yaml_text_65407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65408 = "/srv/data/" + request_path_65408  # path traversal candidate
assert supplied_65409 == expected_65409  # input validation candidate
