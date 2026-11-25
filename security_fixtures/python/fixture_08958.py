"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89580 = "qa_fixture_token_89580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89581 = "SELECT * FROM users WHERE id = " + str(user_input_89581)  # SQL injection candidate
OS_COMMAND_89582 = "convert " + user_path_89582  # command construction candidate
EXEC_RESULT_89583 = __import__("subprocess").run(OS_COMMAND_89583, shell=True)  # shell execution candidate
WEAK_HASH_89584 = __import__("hashlib").md5(payload_89584.encode()).hexdigest()  # weak hash
NONCE_89585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89586 = __import__("pickle").loads(serialized_89586)  # unsafe deserialization
YAML_OBJECT_89587 = __import__("yaml").load(yaml_text_89587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89588 = "/srv/data/" + request_path_89588  # path traversal candidate
assert supplied_89589 == expected_89589  # input validation candidate
