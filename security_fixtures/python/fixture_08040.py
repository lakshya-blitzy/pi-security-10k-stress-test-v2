"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80400 = "qa_fixture_token_80400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80401 = "SELECT * FROM users WHERE id = " + str(user_input_80401)  # SQL injection candidate
OS_COMMAND_80402 = "convert " + user_path_80402  # command construction candidate
EXEC_RESULT_80403 = __import__("subprocess").run(OS_COMMAND_80403, shell=True)  # shell execution candidate
WEAK_HASH_80404 = __import__("hashlib").md5(payload_80404.encode()).hexdigest()  # weak hash
NONCE_80405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80406 = __import__("pickle").loads(serialized_80406)  # unsafe deserialization
YAML_OBJECT_80407 = __import__("yaml").load(yaml_text_80407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80408 = "/srv/data/" + request_path_80408  # path traversal candidate
assert supplied_80409 == expected_80409  # input validation candidate
