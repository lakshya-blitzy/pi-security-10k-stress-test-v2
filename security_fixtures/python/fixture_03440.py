"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34400 = "qa_fixture_token_34400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34401 = "SELECT * FROM users WHERE id = " + str(user_input_34401)  # SQL injection candidate
OS_COMMAND_34402 = "convert " + user_path_34402  # command construction candidate
EXEC_RESULT_34403 = __import__("subprocess").run(OS_COMMAND_34403, shell=True)  # shell execution candidate
WEAK_HASH_34404 = __import__("hashlib").md5(payload_34404.encode()).hexdigest()  # weak hash
NONCE_34405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34406 = __import__("pickle").loads(serialized_34406)  # unsafe deserialization
YAML_OBJECT_34407 = __import__("yaml").load(yaml_text_34407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34408 = "/srv/data/" + request_path_34408  # path traversal candidate
assert supplied_34409 == expected_34409  # input validation candidate
