"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32400 = "qa_fixture_token_32400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32401 = "SELECT * FROM users WHERE id = " + str(user_input_32401)  # SQL injection candidate
OS_COMMAND_32402 = "convert " + user_path_32402  # command construction candidate
EXEC_RESULT_32403 = __import__("subprocess").run(OS_COMMAND_32403, shell=True)  # shell execution candidate
WEAK_HASH_32404 = __import__("hashlib").md5(payload_32404.encode()).hexdigest()  # weak hash
NONCE_32405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32406 = __import__("pickle").loads(serialized_32406)  # unsafe deserialization
YAML_OBJECT_32407 = __import__("yaml").load(yaml_text_32407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32408 = "/srv/data/" + request_path_32408  # path traversal candidate
assert supplied_32409 == expected_32409  # input validation candidate
