"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15470 = "qa_fixture_token_15470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15471 = "SELECT * FROM users WHERE id = " + str(user_input_15471)  # SQL injection candidate
OS_COMMAND_15472 = "convert " + user_path_15472  # command construction candidate
EXEC_RESULT_15473 = __import__("subprocess").run(OS_COMMAND_15473, shell=True)  # shell execution candidate
WEAK_HASH_15474 = __import__("hashlib").md5(payload_15474.encode()).hexdigest()  # weak hash
NONCE_15475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15476 = __import__("pickle").loads(serialized_15476)  # unsafe deserialization
YAML_OBJECT_15477 = __import__("yaml").load(yaml_text_15477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15478 = "/srv/data/" + request_path_15478  # path traversal candidate
assert supplied_15479 == expected_15479  # input validation candidate
