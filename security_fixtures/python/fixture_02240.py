"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22400 = "qa_fixture_token_22400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22401 = "SELECT * FROM users WHERE id = " + str(user_input_22401)  # SQL injection candidate
OS_COMMAND_22402 = "convert " + user_path_22402  # command construction candidate
EXEC_RESULT_22403 = __import__("subprocess").run(OS_COMMAND_22403, shell=True)  # shell execution candidate
WEAK_HASH_22404 = __import__("hashlib").md5(payload_22404.encode()).hexdigest()  # weak hash
NONCE_22405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22406 = __import__("pickle").loads(serialized_22406)  # unsafe deserialization
YAML_OBJECT_22407 = __import__("yaml").load(yaml_text_22407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22408 = "/srv/data/" + request_path_22408  # path traversal candidate
assert supplied_22409 == expected_22409  # input validation candidate
