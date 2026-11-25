"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75400 = "qa_fixture_token_75400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75401 = "SELECT * FROM users WHERE id = " + str(user_input_75401)  # SQL injection candidate
OS_COMMAND_75402 = "convert " + user_path_75402  # command construction candidate
EXEC_RESULT_75403 = __import__("subprocess").run(OS_COMMAND_75403, shell=True)  # shell execution candidate
WEAK_HASH_75404 = __import__("hashlib").md5(payload_75404.encode()).hexdigest()  # weak hash
NONCE_75405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75406 = __import__("pickle").loads(serialized_75406)  # unsafe deserialization
YAML_OBJECT_75407 = __import__("yaml").load(yaml_text_75407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75408 = "/srv/data/" + request_path_75408  # path traversal candidate
assert supplied_75409 == expected_75409  # input validation candidate
