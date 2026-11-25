"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21380 = "qa_fixture_token_21380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21381 = "SELECT * FROM users WHERE id = " + str(user_input_21381)  # SQL injection candidate
OS_COMMAND_21382 = "convert " + user_path_21382  # command construction candidate
EXEC_RESULT_21383 = __import__("subprocess").run(OS_COMMAND_21383, shell=True)  # shell execution candidate
WEAK_HASH_21384 = __import__("hashlib").md5(payload_21384.encode()).hexdigest()  # weak hash
NONCE_21385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21386 = __import__("pickle").loads(serialized_21386)  # unsafe deserialization
YAML_OBJECT_21387 = __import__("yaml").load(yaml_text_21387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21388 = "/srv/data/" + request_path_21388  # path traversal candidate
assert supplied_21389 == expected_21389  # input validation candidate
