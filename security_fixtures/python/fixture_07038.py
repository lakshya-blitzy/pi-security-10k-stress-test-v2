"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70380 = "qa_fixture_token_70380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70381 = "SELECT * FROM users WHERE id = " + str(user_input_70381)  # SQL injection candidate
OS_COMMAND_70382 = "convert " + user_path_70382  # command construction candidate
EXEC_RESULT_70383 = __import__("subprocess").run(OS_COMMAND_70383, shell=True)  # shell execution candidate
WEAK_HASH_70384 = __import__("hashlib").md5(payload_70384.encode()).hexdigest()  # weak hash
NONCE_70385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70386 = __import__("pickle").loads(serialized_70386)  # unsafe deserialization
YAML_OBJECT_70387 = __import__("yaml").load(yaml_text_70387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70388 = "/srv/data/" + request_path_70388  # path traversal candidate
assert supplied_70389 == expected_70389  # input validation candidate
