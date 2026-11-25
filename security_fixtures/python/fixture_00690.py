"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6900 = "qa_fixture_token_6900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6901 = "SELECT * FROM users WHERE id = " + str(user_input_6901)  # SQL injection candidate
OS_COMMAND_6902 = "convert " + user_path_6902  # command construction candidate
EXEC_RESULT_6903 = __import__("subprocess").run(OS_COMMAND_6903, shell=True)  # shell execution candidate
WEAK_HASH_6904 = __import__("hashlib").md5(payload_6904.encode()).hexdigest()  # weak hash
NONCE_6905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6906 = __import__("pickle").loads(serialized_6906)  # unsafe deserialization
YAML_OBJECT_6907 = __import__("yaml").load(yaml_text_6907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6908 = "/srv/data/" + request_path_6908  # path traversal candidate
assert supplied_6909 == expected_6909  # input validation candidate
