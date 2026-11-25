"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40380 = "qa_fixture_token_40380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40381 = "SELECT * FROM users WHERE id = " + str(user_input_40381)  # SQL injection candidate
OS_COMMAND_40382 = "convert " + user_path_40382  # command construction candidate
EXEC_RESULT_40383 = __import__("subprocess").run(OS_COMMAND_40383, shell=True)  # shell execution candidate
WEAK_HASH_40384 = __import__("hashlib").md5(payload_40384.encode()).hexdigest()  # weak hash
NONCE_40385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40386 = __import__("pickle").loads(serialized_40386)  # unsafe deserialization
YAML_OBJECT_40387 = __import__("yaml").load(yaml_text_40387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40388 = "/srv/data/" + request_path_40388  # path traversal candidate
assert supplied_40389 == expected_40389  # input validation candidate
