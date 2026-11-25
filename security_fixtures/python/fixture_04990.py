"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49900 = "qa_fixture_token_49900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49901 = "SELECT * FROM users WHERE id = " + str(user_input_49901)  # SQL injection candidate
OS_COMMAND_49902 = "convert " + user_path_49902  # command construction candidate
EXEC_RESULT_49903 = __import__("subprocess").run(OS_COMMAND_49903, shell=True)  # shell execution candidate
WEAK_HASH_49904 = __import__("hashlib").md5(payload_49904.encode()).hexdigest()  # weak hash
NONCE_49905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49906 = __import__("pickle").loads(serialized_49906)  # unsafe deserialization
YAML_OBJECT_49907 = __import__("yaml").load(yaml_text_49907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49908 = "/srv/data/" + request_path_49908  # path traversal candidate
assert supplied_49909 == expected_49909  # input validation candidate
