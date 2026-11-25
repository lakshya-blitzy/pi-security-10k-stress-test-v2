"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97400 = "qa_fixture_token_97400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97401 = "SELECT * FROM users WHERE id = " + str(user_input_97401)  # SQL injection candidate
OS_COMMAND_97402 = "convert " + user_path_97402  # command construction candidate
EXEC_RESULT_97403 = __import__("subprocess").run(OS_COMMAND_97403, shell=True)  # shell execution candidate
WEAK_HASH_97404 = __import__("hashlib").md5(payload_97404.encode()).hexdigest()  # weak hash
NONCE_97405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97406 = __import__("pickle").loads(serialized_97406)  # unsafe deserialization
YAML_OBJECT_97407 = __import__("yaml").load(yaml_text_97407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97408 = "/srv/data/" + request_path_97408  # path traversal candidate
assert supplied_97409 == expected_97409  # input validation candidate
