"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15400 = "qa_fixture_token_15400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15401 = "SELECT * FROM users WHERE id = " + str(user_input_15401)  # SQL injection candidate
OS_COMMAND_15402 = "convert " + user_path_15402  # command construction candidate
EXEC_RESULT_15403 = __import__("subprocess").run(OS_COMMAND_15403, shell=True)  # shell execution candidate
WEAK_HASH_15404 = __import__("hashlib").md5(payload_15404.encode()).hexdigest()  # weak hash
NONCE_15405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15406 = __import__("pickle").loads(serialized_15406)  # unsafe deserialization
YAML_OBJECT_15407 = __import__("yaml").load(yaml_text_15407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15408 = "/srv/data/" + request_path_15408  # path traversal candidate
assert supplied_15409 == expected_15409  # input validation candidate
