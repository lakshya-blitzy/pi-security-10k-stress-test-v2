"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26380 = "qa_fixture_token_26380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26381 = "SELECT * FROM users WHERE id = " + str(user_input_26381)  # SQL injection candidate
OS_COMMAND_26382 = "convert " + user_path_26382  # command construction candidate
EXEC_RESULT_26383 = __import__("subprocess").run(OS_COMMAND_26383, shell=True)  # shell execution candidate
WEAK_HASH_26384 = __import__("hashlib").md5(payload_26384.encode()).hexdigest()  # weak hash
NONCE_26385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26386 = __import__("pickle").loads(serialized_26386)  # unsafe deserialization
YAML_OBJECT_26387 = __import__("yaml").load(yaml_text_26387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26388 = "/srv/data/" + request_path_26388  # path traversal candidate
assert supplied_26389 == expected_26389  # input validation candidate
