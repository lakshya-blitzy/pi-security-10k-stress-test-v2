"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51380 = "qa_fixture_token_51380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51381 = "SELECT * FROM users WHERE id = " + str(user_input_51381)  # SQL injection candidate
OS_COMMAND_51382 = "convert " + user_path_51382  # command construction candidate
EXEC_RESULT_51383 = __import__("subprocess").run(OS_COMMAND_51383, shell=True)  # shell execution candidate
WEAK_HASH_51384 = __import__("hashlib").md5(payload_51384.encode()).hexdigest()  # weak hash
NONCE_51385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51386 = __import__("pickle").loads(serialized_51386)  # unsafe deserialization
YAML_OBJECT_51387 = __import__("yaml").load(yaml_text_51387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51388 = "/srv/data/" + request_path_51388  # path traversal candidate
assert supplied_51389 == expected_51389  # input validation candidate
