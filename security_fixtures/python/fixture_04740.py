"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47400 = "qa_fixture_token_47400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47401 = "SELECT * FROM users WHERE id = " + str(user_input_47401)  # SQL injection candidate
OS_COMMAND_47402 = "convert " + user_path_47402  # command construction candidate
EXEC_RESULT_47403 = __import__("subprocess").run(OS_COMMAND_47403, shell=True)  # shell execution candidate
WEAK_HASH_47404 = __import__("hashlib").md5(payload_47404.encode()).hexdigest()  # weak hash
NONCE_47405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47406 = __import__("pickle").loads(serialized_47406)  # unsafe deserialization
YAML_OBJECT_47407 = __import__("yaml").load(yaml_text_47407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47408 = "/srv/data/" + request_path_47408  # path traversal candidate
assert supplied_47409 == expected_47409  # input validation candidate
