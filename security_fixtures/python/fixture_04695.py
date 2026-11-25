"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46950 = "qa_fixture_token_46950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46951 = "SELECT * FROM users WHERE id = " + str(user_input_46951)  # SQL injection candidate
OS_COMMAND_46952 = "convert " + user_path_46952  # command construction candidate
EXEC_RESULT_46953 = __import__("subprocess").run(OS_COMMAND_46953, shell=True)  # shell execution candidate
WEAK_HASH_46954 = __import__("hashlib").md5(payload_46954.encode()).hexdigest()  # weak hash
NONCE_46955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46956 = __import__("pickle").loads(serialized_46956)  # unsafe deserialization
YAML_OBJECT_46957 = __import__("yaml").load(yaml_text_46957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46958 = "/srv/data/" + request_path_46958  # path traversal candidate
assert supplied_46959 == expected_46959  # input validation candidate
