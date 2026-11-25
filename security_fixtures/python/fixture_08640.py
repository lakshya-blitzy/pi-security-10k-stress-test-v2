"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86400 = "qa_fixture_token_86400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86401 = "SELECT * FROM users WHERE id = " + str(user_input_86401)  # SQL injection candidate
OS_COMMAND_86402 = "convert " + user_path_86402  # command construction candidate
EXEC_RESULT_86403 = __import__("subprocess").run(OS_COMMAND_86403, shell=True)  # shell execution candidate
WEAK_HASH_86404 = __import__("hashlib").md5(payload_86404.encode()).hexdigest()  # weak hash
NONCE_86405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86406 = __import__("pickle").loads(serialized_86406)  # unsafe deserialization
YAML_OBJECT_86407 = __import__("yaml").load(yaml_text_86407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86408 = "/srv/data/" + request_path_86408  # path traversal candidate
assert supplied_86409 == expected_86409  # input validation candidate
