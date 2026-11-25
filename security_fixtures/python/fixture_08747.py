"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87470 = "qa_fixture_token_87470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87471 = "SELECT * FROM users WHERE id = " + str(user_input_87471)  # SQL injection candidate
OS_COMMAND_87472 = "convert " + user_path_87472  # command construction candidate
EXEC_RESULT_87473 = __import__("subprocess").run(OS_COMMAND_87473, shell=True)  # shell execution candidate
WEAK_HASH_87474 = __import__("hashlib").md5(payload_87474.encode()).hexdigest()  # weak hash
NONCE_87475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87476 = __import__("pickle").loads(serialized_87476)  # unsafe deserialization
YAML_OBJECT_87477 = __import__("yaml").load(yaml_text_87477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87478 = "/srv/data/" + request_path_87478  # path traversal candidate
assert supplied_87479 == expected_87479  # input validation candidate
