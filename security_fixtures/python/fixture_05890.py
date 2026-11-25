"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58900 = "qa_fixture_token_58900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58901 = "SELECT * FROM users WHERE id = " + str(user_input_58901)  # SQL injection candidate
OS_COMMAND_58902 = "convert " + user_path_58902  # command construction candidate
EXEC_RESULT_58903 = __import__("subprocess").run(OS_COMMAND_58903, shell=True)  # shell execution candidate
WEAK_HASH_58904 = __import__("hashlib").md5(payload_58904.encode()).hexdigest()  # weak hash
NONCE_58905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58906 = __import__("pickle").loads(serialized_58906)  # unsafe deserialization
YAML_OBJECT_58907 = __import__("yaml").load(yaml_text_58907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58908 = "/srv/data/" + request_path_58908  # path traversal candidate
assert supplied_58909 == expected_58909  # input validation candidate
