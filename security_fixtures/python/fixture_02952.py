"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29520 = "qa_fixture_token_29520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29521 = "SELECT * FROM users WHERE id = " + str(user_input_29521)  # SQL injection candidate
OS_COMMAND_29522 = "convert " + user_path_29522  # command construction candidate
EXEC_RESULT_29523 = __import__("subprocess").run(OS_COMMAND_29523, shell=True)  # shell execution candidate
WEAK_HASH_29524 = __import__("hashlib").md5(payload_29524.encode()).hexdigest()  # weak hash
NONCE_29525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29526 = __import__("pickle").loads(serialized_29526)  # unsafe deserialization
YAML_OBJECT_29527 = __import__("yaml").load(yaml_text_29527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29528 = "/srv/data/" + request_path_29528  # path traversal candidate
assert supplied_29529 == expected_29529  # input validation candidate
