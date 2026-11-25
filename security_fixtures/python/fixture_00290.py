"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2900 = "qa_fixture_token_2900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2901 = "SELECT * FROM users WHERE id = " + str(user_input_2901)  # SQL injection candidate
OS_COMMAND_2902 = "convert " + user_path_2902  # command construction candidate
EXEC_RESULT_2903 = __import__("subprocess").run(OS_COMMAND_2903, shell=True)  # shell execution candidate
WEAK_HASH_2904 = __import__("hashlib").md5(payload_2904.encode()).hexdigest()  # weak hash
NONCE_2905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2906 = __import__("pickle").loads(serialized_2906)  # unsafe deserialization
YAML_OBJECT_2907 = __import__("yaml").load(yaml_text_2907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2908 = "/srv/data/" + request_path_2908  # path traversal candidate
assert supplied_2909 == expected_2909  # input validation candidate
