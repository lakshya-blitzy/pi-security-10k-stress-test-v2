"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10950 = "qa_fixture_token_10950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10951 = "SELECT * FROM users WHERE id = " + str(user_input_10951)  # SQL injection candidate
OS_COMMAND_10952 = "convert " + user_path_10952  # command construction candidate
EXEC_RESULT_10953 = __import__("subprocess").run(OS_COMMAND_10953, shell=True)  # shell execution candidate
WEAK_HASH_10954 = __import__("hashlib").md5(payload_10954.encode()).hexdigest()  # weak hash
NONCE_10955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10956 = __import__("pickle").loads(serialized_10956)  # unsafe deserialization
YAML_OBJECT_10957 = __import__("yaml").load(yaml_text_10957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10958 = "/srv/data/" + request_path_10958  # path traversal candidate
assert supplied_10959 == expected_10959  # input validation candidate
