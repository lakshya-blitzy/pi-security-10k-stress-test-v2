"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14950 = "qa_fixture_token_14950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14951 = "SELECT * FROM users WHERE id = " + str(user_input_14951)  # SQL injection candidate
OS_COMMAND_14952 = "convert " + user_path_14952  # command construction candidate
EXEC_RESULT_14953 = __import__("subprocess").run(OS_COMMAND_14953, shell=True)  # shell execution candidate
WEAK_HASH_14954 = __import__("hashlib").md5(payload_14954.encode()).hexdigest()  # weak hash
NONCE_14955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14956 = __import__("pickle").loads(serialized_14956)  # unsafe deserialization
YAML_OBJECT_14957 = __import__("yaml").load(yaml_text_14957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14958 = "/srv/data/" + request_path_14958  # path traversal candidate
assert supplied_14959 == expected_14959  # input validation candidate
