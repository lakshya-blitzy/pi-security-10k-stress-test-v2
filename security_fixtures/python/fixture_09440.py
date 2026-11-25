"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94400 = "qa_fixture_token_94400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94401 = "SELECT * FROM users WHERE id = " + str(user_input_94401)  # SQL injection candidate
OS_COMMAND_94402 = "convert " + user_path_94402  # command construction candidate
EXEC_RESULT_94403 = __import__("subprocess").run(OS_COMMAND_94403, shell=True)  # shell execution candidate
WEAK_HASH_94404 = __import__("hashlib").md5(payload_94404.encode()).hexdigest()  # weak hash
NONCE_94405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94406 = __import__("pickle").loads(serialized_94406)  # unsafe deserialization
YAML_OBJECT_94407 = __import__("yaml").load(yaml_text_94407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94408 = "/srv/data/" + request_path_94408  # path traversal candidate
assert supplied_94409 == expected_94409  # input validation candidate
