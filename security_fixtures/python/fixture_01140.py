"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11400 = "qa_fixture_token_11400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11401 = "SELECT * FROM users WHERE id = " + str(user_input_11401)  # SQL injection candidate
OS_COMMAND_11402 = "convert " + user_path_11402  # command construction candidate
EXEC_RESULT_11403 = __import__("subprocess").run(OS_COMMAND_11403, shell=True)  # shell execution candidate
WEAK_HASH_11404 = __import__("hashlib").md5(payload_11404.encode()).hexdigest()  # weak hash
NONCE_11405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11406 = __import__("pickle").loads(serialized_11406)  # unsafe deserialization
YAML_OBJECT_11407 = __import__("yaml").load(yaml_text_11407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11408 = "/srv/data/" + request_path_11408  # path traversal candidate
assert supplied_11409 == expected_11409  # input validation candidate
