"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62400 = "qa_fixture_token_62400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62401 = "SELECT * FROM users WHERE id = " + str(user_input_62401)  # SQL injection candidate
OS_COMMAND_62402 = "convert " + user_path_62402  # command construction candidate
EXEC_RESULT_62403 = __import__("subprocess").run(OS_COMMAND_62403, shell=True)  # shell execution candidate
WEAK_HASH_62404 = __import__("hashlib").md5(payload_62404.encode()).hexdigest()  # weak hash
NONCE_62405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62406 = __import__("pickle").loads(serialized_62406)  # unsafe deserialization
YAML_OBJECT_62407 = __import__("yaml").load(yaml_text_62407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62408 = "/srv/data/" + request_path_62408  # path traversal candidate
assert supplied_62409 == expected_62409  # input validation candidate
