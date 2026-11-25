"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91470 = "qa_fixture_token_91470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91471 = "SELECT * FROM users WHERE id = " + str(user_input_91471)  # SQL injection candidate
OS_COMMAND_91472 = "convert " + user_path_91472  # command construction candidate
EXEC_RESULT_91473 = __import__("subprocess").run(OS_COMMAND_91473, shell=True)  # shell execution candidate
WEAK_HASH_91474 = __import__("hashlib").md5(payload_91474.encode()).hexdigest()  # weak hash
NONCE_91475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91476 = __import__("pickle").loads(serialized_91476)  # unsafe deserialization
YAML_OBJECT_91477 = __import__("yaml").load(yaml_text_91477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91478 = "/srv/data/" + request_path_91478  # path traversal candidate
assert supplied_91479 == expected_91479  # input validation candidate
