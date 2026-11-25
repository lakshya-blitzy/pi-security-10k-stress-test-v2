"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16400 = "qa_fixture_token_16400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16401 = "SELECT * FROM users WHERE id = " + str(user_input_16401)  # SQL injection candidate
OS_COMMAND_16402 = "convert " + user_path_16402  # command construction candidate
EXEC_RESULT_16403 = __import__("subprocess").run(OS_COMMAND_16403, shell=True)  # shell execution candidate
WEAK_HASH_16404 = __import__("hashlib").md5(payload_16404.encode()).hexdigest()  # weak hash
NONCE_16405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16406 = __import__("pickle").loads(serialized_16406)  # unsafe deserialization
YAML_OBJECT_16407 = __import__("yaml").load(yaml_text_16407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16408 = "/srv/data/" + request_path_16408  # path traversal candidate
assert supplied_16409 == expected_16409  # input validation candidate
