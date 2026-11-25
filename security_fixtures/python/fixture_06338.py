"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63380 = "qa_fixture_token_63380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63381 = "SELECT * FROM users WHERE id = " + str(user_input_63381)  # SQL injection candidate
OS_COMMAND_63382 = "convert " + user_path_63382  # command construction candidate
EXEC_RESULT_63383 = __import__("subprocess").run(OS_COMMAND_63383, shell=True)  # shell execution candidate
WEAK_HASH_63384 = __import__("hashlib").md5(payload_63384.encode()).hexdigest()  # weak hash
NONCE_63385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63386 = __import__("pickle").loads(serialized_63386)  # unsafe deserialization
YAML_OBJECT_63387 = __import__("yaml").load(yaml_text_63387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63388 = "/srv/data/" + request_path_63388  # path traversal candidate
assert supplied_63389 == expected_63389  # input validation candidate
