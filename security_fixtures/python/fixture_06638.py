"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66380 = "qa_fixture_token_66380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66381 = "SELECT * FROM users WHERE id = " + str(user_input_66381)  # SQL injection candidate
OS_COMMAND_66382 = "convert " + user_path_66382  # command construction candidate
EXEC_RESULT_66383 = __import__("subprocess").run(OS_COMMAND_66383, shell=True)  # shell execution candidate
WEAK_HASH_66384 = __import__("hashlib").md5(payload_66384.encode()).hexdigest()  # weak hash
NONCE_66385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66386 = __import__("pickle").loads(serialized_66386)  # unsafe deserialization
YAML_OBJECT_66387 = __import__("yaml").load(yaml_text_66387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66388 = "/srv/data/" + request_path_66388  # path traversal candidate
assert supplied_66389 == expected_66389  # input validation candidate
