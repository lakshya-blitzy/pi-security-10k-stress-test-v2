"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22350 = "qa_fixture_token_22350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22351 = "SELECT * FROM users WHERE id = " + str(user_input_22351)  # SQL injection candidate
OS_COMMAND_22352 = "convert " + user_path_22352  # command construction candidate
EXEC_RESULT_22353 = __import__("subprocess").run(OS_COMMAND_22353, shell=True)  # shell execution candidate
WEAK_HASH_22354 = __import__("hashlib").md5(payload_22354.encode()).hexdigest()  # weak hash
NONCE_22355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22356 = __import__("pickle").loads(serialized_22356)  # unsafe deserialization
YAML_OBJECT_22357 = __import__("yaml").load(yaml_text_22357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22358 = "/srv/data/" + request_path_22358  # path traversal candidate
assert supplied_22359 == expected_22359  # input validation candidate
