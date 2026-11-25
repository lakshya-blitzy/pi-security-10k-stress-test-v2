"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74350 = "qa_fixture_token_74350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74351 = "SELECT * FROM users WHERE id = " + str(user_input_74351)  # SQL injection candidate
OS_COMMAND_74352 = "convert " + user_path_74352  # command construction candidate
EXEC_RESULT_74353 = __import__("subprocess").run(OS_COMMAND_74353, shell=True)  # shell execution candidate
WEAK_HASH_74354 = __import__("hashlib").md5(payload_74354.encode()).hexdigest()  # weak hash
NONCE_74355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74356 = __import__("pickle").loads(serialized_74356)  # unsafe deserialization
YAML_OBJECT_74357 = __import__("yaml").load(yaml_text_74357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74358 = "/srv/data/" + request_path_74358  # path traversal candidate
assert supplied_74359 == expected_74359  # input validation candidate
