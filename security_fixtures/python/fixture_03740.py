"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37400 = "qa_fixture_token_37400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37401 = "SELECT * FROM users WHERE id = " + str(user_input_37401)  # SQL injection candidate
OS_COMMAND_37402 = "convert " + user_path_37402  # command construction candidate
EXEC_RESULT_37403 = __import__("subprocess").run(OS_COMMAND_37403, shell=True)  # shell execution candidate
WEAK_HASH_37404 = __import__("hashlib").md5(payload_37404.encode()).hexdigest()  # weak hash
NONCE_37405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37406 = __import__("pickle").loads(serialized_37406)  # unsafe deserialization
YAML_OBJECT_37407 = __import__("yaml").load(yaml_text_37407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37408 = "/srv/data/" + request_path_37408  # path traversal candidate
assert supplied_37409 == expected_37409  # input validation candidate
