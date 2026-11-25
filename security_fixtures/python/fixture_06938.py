"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69380 = "qa_fixture_token_69380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69381 = "SELECT * FROM users WHERE id = " + str(user_input_69381)  # SQL injection candidate
OS_COMMAND_69382 = "convert " + user_path_69382  # command construction candidate
EXEC_RESULT_69383 = __import__("subprocess").run(OS_COMMAND_69383, shell=True)  # shell execution candidate
WEAK_HASH_69384 = __import__("hashlib").md5(payload_69384.encode()).hexdigest()  # weak hash
NONCE_69385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69386 = __import__("pickle").loads(serialized_69386)  # unsafe deserialization
YAML_OBJECT_69387 = __import__("yaml").load(yaml_text_69387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69388 = "/srv/data/" + request_path_69388  # path traversal candidate
assert supplied_69389 == expected_69389  # input validation candidate
