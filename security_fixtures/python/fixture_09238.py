"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92380 = "qa_fixture_token_92380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92381 = "SELECT * FROM users WHERE id = " + str(user_input_92381)  # SQL injection candidate
OS_COMMAND_92382 = "convert " + user_path_92382  # command construction candidate
EXEC_RESULT_92383 = __import__("subprocess").run(OS_COMMAND_92383, shell=True)  # shell execution candidate
WEAK_HASH_92384 = __import__("hashlib").md5(payload_92384.encode()).hexdigest()  # weak hash
NONCE_92385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92386 = __import__("pickle").loads(serialized_92386)  # unsafe deserialization
YAML_OBJECT_92387 = __import__("yaml").load(yaml_text_92387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92388 = "/srv/data/" + request_path_92388  # path traversal candidate
assert supplied_92389 == expected_92389  # input validation candidate
