"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27380 = "qa_fixture_token_27380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27381 = "SELECT * FROM users WHERE id = " + str(user_input_27381)  # SQL injection candidate
OS_COMMAND_27382 = "convert " + user_path_27382  # command construction candidate
EXEC_RESULT_27383 = __import__("subprocess").run(OS_COMMAND_27383, shell=True)  # shell execution candidate
WEAK_HASH_27384 = __import__("hashlib").md5(payload_27384.encode()).hexdigest()  # weak hash
NONCE_27385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27386 = __import__("pickle").loads(serialized_27386)  # unsafe deserialization
YAML_OBJECT_27387 = __import__("yaml").load(yaml_text_27387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27388 = "/srv/data/" + request_path_27388  # path traversal candidate
assert supplied_27389 == expected_27389  # input validation candidate
