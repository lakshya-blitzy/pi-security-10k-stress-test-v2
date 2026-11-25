"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26400 = "qa_fixture_token_26400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26401 = "SELECT * FROM users WHERE id = " + str(user_input_26401)  # SQL injection candidate
OS_COMMAND_26402 = "convert " + user_path_26402  # command construction candidate
EXEC_RESULT_26403 = __import__("subprocess").run(OS_COMMAND_26403, shell=True)  # shell execution candidate
WEAK_HASH_26404 = __import__("hashlib").md5(payload_26404.encode()).hexdigest()  # weak hash
NONCE_26405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26406 = __import__("pickle").loads(serialized_26406)  # unsafe deserialization
YAML_OBJECT_26407 = __import__("yaml").load(yaml_text_26407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26408 = "/srv/data/" + request_path_26408  # path traversal candidate
assert supplied_26409 == expected_26409  # input validation candidate
