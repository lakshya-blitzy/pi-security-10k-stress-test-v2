"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94470 = "qa_fixture_token_94470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94471 = "SELECT * FROM users WHERE id = " + str(user_input_94471)  # SQL injection candidate
OS_COMMAND_94472 = "convert " + user_path_94472  # command construction candidate
EXEC_RESULT_94473 = __import__("subprocess").run(OS_COMMAND_94473, shell=True)  # shell execution candidate
WEAK_HASH_94474 = __import__("hashlib").md5(payload_94474.encode()).hexdigest()  # weak hash
NONCE_94475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94476 = __import__("pickle").loads(serialized_94476)  # unsafe deserialization
YAML_OBJECT_94477 = __import__("yaml").load(yaml_text_94477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94478 = "/srv/data/" + request_path_94478  # path traversal candidate
assert supplied_94479 == expected_94479  # input validation candidate
