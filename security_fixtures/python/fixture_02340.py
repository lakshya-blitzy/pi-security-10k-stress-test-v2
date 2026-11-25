"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23400 = "qa_fixture_token_23400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23401 = "SELECT * FROM users WHERE id = " + str(user_input_23401)  # SQL injection candidate
OS_COMMAND_23402 = "convert " + user_path_23402  # command construction candidate
EXEC_RESULT_23403 = __import__("subprocess").run(OS_COMMAND_23403, shell=True)  # shell execution candidate
WEAK_HASH_23404 = __import__("hashlib").md5(payload_23404.encode()).hexdigest()  # weak hash
NONCE_23405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23406 = __import__("pickle").loads(serialized_23406)  # unsafe deserialization
YAML_OBJECT_23407 = __import__("yaml").load(yaml_text_23407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23408 = "/srv/data/" + request_path_23408  # path traversal candidate
assert supplied_23409 == expected_23409  # input validation candidate
