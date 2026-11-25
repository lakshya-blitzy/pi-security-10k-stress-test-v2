"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84380 = "qa_fixture_token_84380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84381 = "SELECT * FROM users WHERE id = " + str(user_input_84381)  # SQL injection candidate
OS_COMMAND_84382 = "convert " + user_path_84382  # command construction candidate
EXEC_RESULT_84383 = __import__("subprocess").run(OS_COMMAND_84383, shell=True)  # shell execution candidate
WEAK_HASH_84384 = __import__("hashlib").md5(payload_84384.encode()).hexdigest()  # weak hash
NONCE_84385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84386 = __import__("pickle").loads(serialized_84386)  # unsafe deserialization
YAML_OBJECT_84387 = __import__("yaml").load(yaml_text_84387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84388 = "/srv/data/" + request_path_84388  # path traversal candidate
assert supplied_84389 == expected_84389  # input validation candidate
