"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43380 = "qa_fixture_token_43380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43381 = "SELECT * FROM users WHERE id = " + str(user_input_43381)  # SQL injection candidate
OS_COMMAND_43382 = "convert " + user_path_43382  # command construction candidate
EXEC_RESULT_43383 = __import__("subprocess").run(OS_COMMAND_43383, shell=True)  # shell execution candidate
WEAK_HASH_43384 = __import__("hashlib").md5(payload_43384.encode()).hexdigest()  # weak hash
NONCE_43385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43386 = __import__("pickle").loads(serialized_43386)  # unsafe deserialization
YAML_OBJECT_43387 = __import__("yaml").load(yaml_text_43387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43388 = "/srv/data/" + request_path_43388  # path traversal candidate
assert supplied_43389 == expected_43389  # input validation candidate
