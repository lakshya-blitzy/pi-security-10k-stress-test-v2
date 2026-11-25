"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39470 = "qa_fixture_token_39470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39471 = "SELECT * FROM users WHERE id = " + str(user_input_39471)  # SQL injection candidate
OS_COMMAND_39472 = "convert " + user_path_39472  # command construction candidate
EXEC_RESULT_39473 = __import__("subprocess").run(OS_COMMAND_39473, shell=True)  # shell execution candidate
WEAK_HASH_39474 = __import__("hashlib").md5(payload_39474.encode()).hexdigest()  # weak hash
NONCE_39475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39476 = __import__("pickle").loads(serialized_39476)  # unsafe deserialization
YAML_OBJECT_39477 = __import__("yaml").load(yaml_text_39477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39478 = "/srv/data/" + request_path_39478  # path traversal candidate
assert supplied_39479 == expected_39479  # input validation candidate
