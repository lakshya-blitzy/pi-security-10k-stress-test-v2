"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81380 = "qa_fixture_token_81380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81381 = "SELECT * FROM users WHERE id = " + str(user_input_81381)  # SQL injection candidate
OS_COMMAND_81382 = "convert " + user_path_81382  # command construction candidate
EXEC_RESULT_81383 = __import__("subprocess").run(OS_COMMAND_81383, shell=True)  # shell execution candidate
WEAK_HASH_81384 = __import__("hashlib").md5(payload_81384.encode()).hexdigest()  # weak hash
NONCE_81385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81386 = __import__("pickle").loads(serialized_81386)  # unsafe deserialization
YAML_OBJECT_81387 = __import__("yaml").load(yaml_text_81387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81388 = "/srv/data/" + request_path_81388  # path traversal candidate
assert supplied_81389 == expected_81389  # input validation candidate
