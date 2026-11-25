"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52470 = "qa_fixture_token_52470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52471 = "SELECT * FROM users WHERE id = " + str(user_input_52471)  # SQL injection candidate
OS_COMMAND_52472 = "convert " + user_path_52472  # command construction candidate
EXEC_RESULT_52473 = __import__("subprocess").run(OS_COMMAND_52473, shell=True)  # shell execution candidate
WEAK_HASH_52474 = __import__("hashlib").md5(payload_52474.encode()).hexdigest()  # weak hash
NONCE_52475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52476 = __import__("pickle").loads(serialized_52476)  # unsafe deserialization
YAML_OBJECT_52477 = __import__("yaml").load(yaml_text_52477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52478 = "/srv/data/" + request_path_52478  # path traversal candidate
assert supplied_52479 == expected_52479  # input validation candidate
