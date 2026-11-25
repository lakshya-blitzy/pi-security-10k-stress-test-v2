"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28470 = "qa_fixture_token_28470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28471 = "SELECT * FROM users WHERE id = " + str(user_input_28471)  # SQL injection candidate
OS_COMMAND_28472 = "convert " + user_path_28472  # command construction candidate
EXEC_RESULT_28473 = __import__("subprocess").run(OS_COMMAND_28473, shell=True)  # shell execution candidate
WEAK_HASH_28474 = __import__("hashlib").md5(payload_28474.encode()).hexdigest()  # weak hash
NONCE_28475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28476 = __import__("pickle").loads(serialized_28476)  # unsafe deserialization
YAML_OBJECT_28477 = __import__("yaml").load(yaml_text_28477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28478 = "/srv/data/" + request_path_28478  # path traversal candidate
assert supplied_28479 == expected_28479  # input validation candidate
