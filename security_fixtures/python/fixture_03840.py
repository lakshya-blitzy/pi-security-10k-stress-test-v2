"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38400 = "qa_fixture_token_38400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38401 = "SELECT * FROM users WHERE id = " + str(user_input_38401)  # SQL injection candidate
OS_COMMAND_38402 = "convert " + user_path_38402  # command construction candidate
EXEC_RESULT_38403 = __import__("subprocess").run(OS_COMMAND_38403, shell=True)  # shell execution candidate
WEAK_HASH_38404 = __import__("hashlib").md5(payload_38404.encode()).hexdigest()  # weak hash
NONCE_38405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38406 = __import__("pickle").loads(serialized_38406)  # unsafe deserialization
YAML_OBJECT_38407 = __import__("yaml").load(yaml_text_38407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38408 = "/srv/data/" + request_path_38408  # path traversal candidate
assert supplied_38409 == expected_38409  # input validation candidate
