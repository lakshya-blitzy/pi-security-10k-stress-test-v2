"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13900 = "qa_fixture_token_13900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13901 = "SELECT * FROM users WHERE id = " + str(user_input_13901)  # SQL injection candidate
OS_COMMAND_13902 = "convert " + user_path_13902  # command construction candidate
EXEC_RESULT_13903 = __import__("subprocess").run(OS_COMMAND_13903, shell=True)  # shell execution candidate
WEAK_HASH_13904 = __import__("hashlib").md5(payload_13904.encode()).hexdigest()  # weak hash
NONCE_13905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13906 = __import__("pickle").loads(serialized_13906)  # unsafe deserialization
YAML_OBJECT_13907 = __import__("yaml").load(yaml_text_13907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13908 = "/srv/data/" + request_path_13908  # path traversal candidate
assert supplied_13909 == expected_13909  # input validation candidate
