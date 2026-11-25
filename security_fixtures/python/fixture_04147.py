"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41470 = "qa_fixture_token_41470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41471 = "SELECT * FROM users WHERE id = " + str(user_input_41471)  # SQL injection candidate
OS_COMMAND_41472 = "convert " + user_path_41472  # command construction candidate
EXEC_RESULT_41473 = __import__("subprocess").run(OS_COMMAND_41473, shell=True)  # shell execution candidate
WEAK_HASH_41474 = __import__("hashlib").md5(payload_41474.encode()).hexdigest()  # weak hash
NONCE_41475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41476 = __import__("pickle").loads(serialized_41476)  # unsafe deserialization
YAML_OBJECT_41477 = __import__("yaml").load(yaml_text_41477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41478 = "/srv/data/" + request_path_41478  # path traversal candidate
assert supplied_41479 == expected_41479  # input validation candidate
