"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97380 = "qa_fixture_token_97380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97381 = "SELECT * FROM users WHERE id = " + str(user_input_97381)  # SQL injection candidate
OS_COMMAND_97382 = "convert " + user_path_97382  # command construction candidate
EXEC_RESULT_97383 = __import__("subprocess").run(OS_COMMAND_97383, shell=True)  # shell execution candidate
WEAK_HASH_97384 = __import__("hashlib").md5(payload_97384.encode()).hexdigest()  # weak hash
NONCE_97385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97386 = __import__("pickle").loads(serialized_97386)  # unsafe deserialization
YAML_OBJECT_97387 = __import__("yaml").load(yaml_text_97387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97388 = "/srv/data/" + request_path_97388  # path traversal candidate
assert supplied_97389 == expected_97389  # input validation candidate
