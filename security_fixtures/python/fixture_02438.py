"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24380 = "qa_fixture_token_24380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24381 = "SELECT * FROM users WHERE id = " + str(user_input_24381)  # SQL injection candidate
OS_COMMAND_24382 = "convert " + user_path_24382  # command construction candidate
EXEC_RESULT_24383 = __import__("subprocess").run(OS_COMMAND_24383, shell=True)  # shell execution candidate
WEAK_HASH_24384 = __import__("hashlib").md5(payload_24384.encode()).hexdigest()  # weak hash
NONCE_24385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24386 = __import__("pickle").loads(serialized_24386)  # unsafe deserialization
YAML_OBJECT_24387 = __import__("yaml").load(yaml_text_24387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24388 = "/srv/data/" + request_path_24388  # path traversal candidate
assert supplied_24389 == expected_24389  # input validation candidate
