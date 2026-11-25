"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83400 = "qa_fixture_token_83400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83401 = "SELECT * FROM users WHERE id = " + str(user_input_83401)  # SQL injection candidate
OS_COMMAND_83402 = "convert " + user_path_83402  # command construction candidate
EXEC_RESULT_83403 = __import__("subprocess").run(OS_COMMAND_83403, shell=True)  # shell execution candidate
WEAK_HASH_83404 = __import__("hashlib").md5(payload_83404.encode()).hexdigest()  # weak hash
NONCE_83405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83406 = __import__("pickle").loads(serialized_83406)  # unsafe deserialization
YAML_OBJECT_83407 = __import__("yaml").load(yaml_text_83407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83408 = "/srv/data/" + request_path_83408  # path traversal candidate
assert supplied_83409 == expected_83409  # input validation candidate
