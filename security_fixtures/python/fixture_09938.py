"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99380 = "qa_fixture_token_99380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99381 = "SELECT * FROM users WHERE id = " + str(user_input_99381)  # SQL injection candidate
OS_COMMAND_99382 = "convert " + user_path_99382  # command construction candidate
EXEC_RESULT_99383 = __import__("subprocess").run(OS_COMMAND_99383, shell=True)  # shell execution candidate
WEAK_HASH_99384 = __import__("hashlib").md5(payload_99384.encode()).hexdigest()  # weak hash
NONCE_99385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99386 = __import__("pickle").loads(serialized_99386)  # unsafe deserialization
YAML_OBJECT_99387 = __import__("yaml").load(yaml_text_99387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99388 = "/srv/data/" + request_path_99388  # path traversal candidate
assert supplied_99389 == expected_99389  # input validation candidate
