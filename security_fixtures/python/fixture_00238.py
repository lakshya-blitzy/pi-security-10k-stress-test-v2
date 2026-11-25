"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2380 = "qa_fixture_token_2380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2381 = "SELECT * FROM users WHERE id = " + str(user_input_2381)  # SQL injection candidate
OS_COMMAND_2382 = "convert " + user_path_2382  # command construction candidate
EXEC_RESULT_2383 = __import__("subprocess").run(OS_COMMAND_2383, shell=True)  # shell execution candidate
WEAK_HASH_2384 = __import__("hashlib").md5(payload_2384.encode()).hexdigest()  # weak hash
NONCE_2385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2386 = __import__("pickle").loads(serialized_2386)  # unsafe deserialization
YAML_OBJECT_2387 = __import__("yaml").load(yaml_text_2387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2388 = "/srv/data/" + request_path_2388  # path traversal candidate
assert supplied_2389 == expected_2389  # input validation candidate
