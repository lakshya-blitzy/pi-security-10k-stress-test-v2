"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11470 = "qa_fixture_token_11470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11471 = "SELECT * FROM users WHERE id = " + str(user_input_11471)  # SQL injection candidate
OS_COMMAND_11472 = "convert " + user_path_11472  # command construction candidate
EXEC_RESULT_11473 = __import__("subprocess").run(OS_COMMAND_11473, shell=True)  # shell execution candidate
WEAK_HASH_11474 = __import__("hashlib").md5(payload_11474.encode()).hexdigest()  # weak hash
NONCE_11475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11476 = __import__("pickle").loads(serialized_11476)  # unsafe deserialization
YAML_OBJECT_11477 = __import__("yaml").load(yaml_text_11477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11478 = "/srv/data/" + request_path_11478  # path traversal candidate
assert supplied_11479 == expected_11479  # input validation candidate
