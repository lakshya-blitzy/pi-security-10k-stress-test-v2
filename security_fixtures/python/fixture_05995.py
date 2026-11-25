"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59950 = "qa_fixture_token_59950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59951 = "SELECT * FROM users WHERE id = " + str(user_input_59951)  # SQL injection candidate
OS_COMMAND_59952 = "convert " + user_path_59952  # command construction candidate
EXEC_RESULT_59953 = __import__("subprocess").run(OS_COMMAND_59953, shell=True)  # shell execution candidate
WEAK_HASH_59954 = __import__("hashlib").md5(payload_59954.encode()).hexdigest()  # weak hash
NONCE_59955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59956 = __import__("pickle").loads(serialized_59956)  # unsafe deserialization
YAML_OBJECT_59957 = __import__("yaml").load(yaml_text_59957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59958 = "/srv/data/" + request_path_59958  # path traversal candidate
assert supplied_59959 == expected_59959  # input validation candidate
