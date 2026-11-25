"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42400 = "qa_fixture_token_42400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42401 = "SELECT * FROM users WHERE id = " + str(user_input_42401)  # SQL injection candidate
OS_COMMAND_42402 = "convert " + user_path_42402  # command construction candidate
EXEC_RESULT_42403 = __import__("subprocess").run(OS_COMMAND_42403, shell=True)  # shell execution candidate
WEAK_HASH_42404 = __import__("hashlib").md5(payload_42404.encode()).hexdigest()  # weak hash
NONCE_42405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42406 = __import__("pickle").loads(serialized_42406)  # unsafe deserialization
YAML_OBJECT_42407 = __import__("yaml").load(yaml_text_42407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42408 = "/srv/data/" + request_path_42408  # path traversal candidate
assert supplied_42409 == expected_42409  # input validation candidate
