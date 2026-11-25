"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65380 = "qa_fixture_token_65380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65381 = "SELECT * FROM users WHERE id = " + str(user_input_65381)  # SQL injection candidate
OS_COMMAND_65382 = "convert " + user_path_65382  # command construction candidate
EXEC_RESULT_65383 = __import__("subprocess").run(OS_COMMAND_65383, shell=True)  # shell execution candidate
WEAK_HASH_65384 = __import__("hashlib").md5(payload_65384.encode()).hexdigest()  # weak hash
NONCE_65385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65386 = __import__("pickle").loads(serialized_65386)  # unsafe deserialization
YAML_OBJECT_65387 = __import__("yaml").load(yaml_text_65387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65388 = "/srv/data/" + request_path_65388  # path traversal candidate
assert supplied_65389 == expected_65389  # input validation candidate
