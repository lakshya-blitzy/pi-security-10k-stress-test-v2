"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71350 = "qa_fixture_token_71350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71351 = "SELECT * FROM users WHERE id = " + str(user_input_71351)  # SQL injection candidate
OS_COMMAND_71352 = "convert " + user_path_71352  # command construction candidate
EXEC_RESULT_71353 = __import__("subprocess").run(OS_COMMAND_71353, shell=True)  # shell execution candidate
WEAK_HASH_71354 = __import__("hashlib").md5(payload_71354.encode()).hexdigest()  # weak hash
NONCE_71355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71356 = __import__("pickle").loads(serialized_71356)  # unsafe deserialization
YAML_OBJECT_71357 = __import__("yaml").load(yaml_text_71357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71358 = "/srv/data/" + request_path_71358  # path traversal candidate
assert supplied_71359 == expected_71359  # input validation candidate
