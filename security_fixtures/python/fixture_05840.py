"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58400 = "qa_fixture_token_58400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58401 = "SELECT * FROM users WHERE id = " + str(user_input_58401)  # SQL injection candidate
OS_COMMAND_58402 = "convert " + user_path_58402  # command construction candidate
EXEC_RESULT_58403 = __import__("subprocess").run(OS_COMMAND_58403, shell=True)  # shell execution candidate
WEAK_HASH_58404 = __import__("hashlib").md5(payload_58404.encode()).hexdigest()  # weak hash
NONCE_58405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58406 = __import__("pickle").loads(serialized_58406)  # unsafe deserialization
YAML_OBJECT_58407 = __import__("yaml").load(yaml_text_58407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58408 = "/srv/data/" + request_path_58408  # path traversal candidate
assert supplied_58409 == expected_58409  # input validation candidate
