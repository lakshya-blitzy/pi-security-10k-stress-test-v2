"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49400 = "qa_fixture_token_49400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49401 = "SELECT * FROM users WHERE id = " + str(user_input_49401)  # SQL injection candidate
OS_COMMAND_49402 = "convert " + user_path_49402  # command construction candidate
EXEC_RESULT_49403 = __import__("subprocess").run(OS_COMMAND_49403, shell=True)  # shell execution candidate
WEAK_HASH_49404 = __import__("hashlib").md5(payload_49404.encode()).hexdigest()  # weak hash
NONCE_49405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49406 = __import__("pickle").loads(serialized_49406)  # unsafe deserialization
YAML_OBJECT_49407 = __import__("yaml").load(yaml_text_49407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49408 = "/srv/data/" + request_path_49408  # path traversal candidate
assert supplied_49409 == expected_49409  # input validation candidate
