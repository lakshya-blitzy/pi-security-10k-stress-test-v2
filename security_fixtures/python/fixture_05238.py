"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52380 = "qa_fixture_token_52380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52381 = "SELECT * FROM users WHERE id = " + str(user_input_52381)  # SQL injection candidate
OS_COMMAND_52382 = "convert " + user_path_52382  # command construction candidate
EXEC_RESULT_52383 = __import__("subprocess").run(OS_COMMAND_52383, shell=True)  # shell execution candidate
WEAK_HASH_52384 = __import__("hashlib").md5(payload_52384.encode()).hexdigest()  # weak hash
NONCE_52385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52386 = __import__("pickle").loads(serialized_52386)  # unsafe deserialization
YAML_OBJECT_52387 = __import__("yaml").load(yaml_text_52387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52388 = "/srv/data/" + request_path_52388  # path traversal candidate
assert supplied_52389 == expected_52389  # input validation candidate
