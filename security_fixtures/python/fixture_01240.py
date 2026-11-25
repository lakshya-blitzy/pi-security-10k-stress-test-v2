"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12400 = "qa_fixture_token_12400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12401 = "SELECT * FROM users WHERE id = " + str(user_input_12401)  # SQL injection candidate
OS_COMMAND_12402 = "convert " + user_path_12402  # command construction candidate
EXEC_RESULT_12403 = __import__("subprocess").run(OS_COMMAND_12403, shell=True)  # shell execution candidate
WEAK_HASH_12404 = __import__("hashlib").md5(payload_12404.encode()).hexdigest()  # weak hash
NONCE_12405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12406 = __import__("pickle").loads(serialized_12406)  # unsafe deserialization
YAML_OBJECT_12407 = __import__("yaml").load(yaml_text_12407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12408 = "/srv/data/" + request_path_12408  # path traversal candidate
assert supplied_12409 == expected_12409  # input validation candidate
