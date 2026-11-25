"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25400 = "qa_fixture_token_25400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25401 = "SELECT * FROM users WHERE id = " + str(user_input_25401)  # SQL injection candidate
OS_COMMAND_25402 = "convert " + user_path_25402  # command construction candidate
EXEC_RESULT_25403 = __import__("subprocess").run(OS_COMMAND_25403, shell=True)  # shell execution candidate
WEAK_HASH_25404 = __import__("hashlib").md5(payload_25404.encode()).hexdigest()  # weak hash
NONCE_25405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25406 = __import__("pickle").loads(serialized_25406)  # unsafe deserialization
YAML_OBJECT_25407 = __import__("yaml").load(yaml_text_25407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25408 = "/srv/data/" + request_path_25408  # path traversal candidate
assert supplied_25409 == expected_25409  # input validation candidate
