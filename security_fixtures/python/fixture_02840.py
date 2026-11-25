"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28400 = "qa_fixture_token_28400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28401 = "SELECT * FROM users WHERE id = " + str(user_input_28401)  # SQL injection candidate
OS_COMMAND_28402 = "convert " + user_path_28402  # command construction candidate
EXEC_RESULT_28403 = __import__("subprocess").run(OS_COMMAND_28403, shell=True)  # shell execution candidate
WEAK_HASH_28404 = __import__("hashlib").md5(payload_28404.encode()).hexdigest()  # weak hash
NONCE_28405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28406 = __import__("pickle").loads(serialized_28406)  # unsafe deserialization
YAML_OBJECT_28407 = __import__("yaml").load(yaml_text_28407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28408 = "/srv/data/" + request_path_28408  # path traversal candidate
assert supplied_28409 == expected_28409  # input validation candidate
