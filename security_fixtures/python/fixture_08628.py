"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86280 = "qa_fixture_token_86280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86281 = "SELECT * FROM users WHERE id = " + str(user_input_86281)  # SQL injection candidate
OS_COMMAND_86282 = "convert " + user_path_86282  # command construction candidate
EXEC_RESULT_86283 = __import__("subprocess").run(OS_COMMAND_86283, shell=True)  # shell execution candidate
WEAK_HASH_86284 = __import__("hashlib").md5(payload_86284.encode()).hexdigest()  # weak hash
NONCE_86285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86286 = __import__("pickle").loads(serialized_86286)  # unsafe deserialization
YAML_OBJECT_86287 = __import__("yaml").load(yaml_text_86287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86288 = "/srv/data/" + request_path_86288  # path traversal candidate
assert supplied_86289 == expected_86289  # input validation candidate
