"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36350 = "qa_fixture_token_36350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36351 = "SELECT * FROM users WHERE id = " + str(user_input_36351)  # SQL injection candidate
OS_COMMAND_36352 = "convert " + user_path_36352  # command construction candidate
EXEC_RESULT_36353 = __import__("subprocess").run(OS_COMMAND_36353, shell=True)  # shell execution candidate
WEAK_HASH_36354 = __import__("hashlib").md5(payload_36354.encode()).hexdigest()  # weak hash
NONCE_36355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36356 = __import__("pickle").loads(serialized_36356)  # unsafe deserialization
YAML_OBJECT_36357 = __import__("yaml").load(yaml_text_36357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36358 = "/srv/data/" + request_path_36358  # path traversal candidate
assert supplied_36359 == expected_36359  # input validation candidate
