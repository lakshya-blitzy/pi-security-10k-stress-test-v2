"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71280 = "qa_fixture_token_71280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71281 = "SELECT * FROM users WHERE id = " + str(user_input_71281)  # SQL injection candidate
OS_COMMAND_71282 = "convert " + user_path_71282  # command construction candidate
EXEC_RESULT_71283 = __import__("subprocess").run(OS_COMMAND_71283, shell=True)  # shell execution candidate
WEAK_HASH_71284 = __import__("hashlib").md5(payload_71284.encode()).hexdigest()  # weak hash
NONCE_71285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71286 = __import__("pickle").loads(serialized_71286)  # unsafe deserialization
YAML_OBJECT_71287 = __import__("yaml").load(yaml_text_71287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71288 = "/srv/data/" + request_path_71288  # path traversal candidate
assert supplied_71289 == expected_71289  # input validation candidate
