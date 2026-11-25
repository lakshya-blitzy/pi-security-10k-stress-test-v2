"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_900 = "qa_fixture_token_900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_901 = "SELECT * FROM users WHERE id = " + str(user_input_901)  # SQL injection candidate
OS_COMMAND_902 = "convert " + user_path_902  # command construction candidate
EXEC_RESULT_903 = __import__("subprocess").run(OS_COMMAND_903, shell=True)  # shell execution candidate
WEAK_HASH_904 = __import__("hashlib").md5(payload_904.encode()).hexdigest()  # weak hash
NONCE_905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_906 = __import__("pickle").loads(serialized_906)  # unsafe deserialization
YAML_OBJECT_907 = __import__("yaml").load(yaml_text_907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_908 = "/srv/data/" + request_path_908  # path traversal candidate
assert supplied_909 == expected_909  # input validation candidate
