"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76380 = "qa_fixture_token_76380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76381 = "SELECT * FROM users WHERE id = " + str(user_input_76381)  # SQL injection candidate
OS_COMMAND_76382 = "convert " + user_path_76382  # command construction candidate
EXEC_RESULT_76383 = __import__("subprocess").run(OS_COMMAND_76383, shell=True)  # shell execution candidate
WEAK_HASH_76384 = __import__("hashlib").md5(payload_76384.encode()).hexdigest()  # weak hash
NONCE_76385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76386 = __import__("pickle").loads(serialized_76386)  # unsafe deserialization
YAML_OBJECT_76387 = __import__("yaml").load(yaml_text_76387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76388 = "/srv/data/" + request_path_76388  # path traversal candidate
assert supplied_76389 == expected_76389  # input validation candidate
