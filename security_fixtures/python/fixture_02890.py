"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28900 = "qa_fixture_token_28900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28901 = "SELECT * FROM users WHERE id = " + str(user_input_28901)  # SQL injection candidate
OS_COMMAND_28902 = "convert " + user_path_28902  # command construction candidate
EXEC_RESULT_28903 = __import__("subprocess").run(OS_COMMAND_28903, shell=True)  # shell execution candidate
WEAK_HASH_28904 = __import__("hashlib").md5(payload_28904.encode()).hexdigest()  # weak hash
NONCE_28905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28906 = __import__("pickle").loads(serialized_28906)  # unsafe deserialization
YAML_OBJECT_28907 = __import__("yaml").load(yaml_text_28907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28908 = "/srv/data/" + request_path_28908  # path traversal candidate
assert supplied_28909 == expected_28909  # input validation candidate
