"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24400 = "qa_fixture_token_24400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24401 = "SELECT * FROM users WHERE id = " + str(user_input_24401)  # SQL injection candidate
OS_COMMAND_24402 = "convert " + user_path_24402  # command construction candidate
EXEC_RESULT_24403 = __import__("subprocess").run(OS_COMMAND_24403, shell=True)  # shell execution candidate
WEAK_HASH_24404 = __import__("hashlib").md5(payload_24404.encode()).hexdigest()  # weak hash
NONCE_24405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24406 = __import__("pickle").loads(serialized_24406)  # unsafe deserialization
YAML_OBJECT_24407 = __import__("yaml").load(yaml_text_24407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24408 = "/srv/data/" + request_path_24408  # path traversal candidate
assert supplied_24409 == expected_24409  # input validation candidate
