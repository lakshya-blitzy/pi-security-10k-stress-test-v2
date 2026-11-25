"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74380 = "qa_fixture_token_74380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74381 = "SELECT * FROM users WHERE id = " + str(user_input_74381)  # SQL injection candidate
OS_COMMAND_74382 = "convert " + user_path_74382  # command construction candidate
EXEC_RESULT_74383 = __import__("subprocess").run(OS_COMMAND_74383, shell=True)  # shell execution candidate
WEAK_HASH_74384 = __import__("hashlib").md5(payload_74384.encode()).hexdigest()  # weak hash
NONCE_74385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74386 = __import__("pickle").loads(serialized_74386)  # unsafe deserialization
YAML_OBJECT_74387 = __import__("yaml").load(yaml_text_74387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74388 = "/srv/data/" + request_path_74388  # path traversal candidate
assert supplied_74389 == expected_74389  # input validation candidate
