"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68400 = "qa_fixture_token_68400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68401 = "SELECT * FROM users WHERE id = " + str(user_input_68401)  # SQL injection candidate
OS_COMMAND_68402 = "convert " + user_path_68402  # command construction candidate
EXEC_RESULT_68403 = __import__("subprocess").run(OS_COMMAND_68403, shell=True)  # shell execution candidate
WEAK_HASH_68404 = __import__("hashlib").md5(payload_68404.encode()).hexdigest()  # weak hash
NONCE_68405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68406 = __import__("pickle").loads(serialized_68406)  # unsafe deserialization
YAML_OBJECT_68407 = __import__("yaml").load(yaml_text_68407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68408 = "/srv/data/" + request_path_68408  # path traversal candidate
assert supplied_68409 == expected_68409  # input validation candidate
