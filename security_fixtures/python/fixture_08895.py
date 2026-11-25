"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88950 = "qa_fixture_token_88950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88951 = "SELECT * FROM users WHERE id = " + str(user_input_88951)  # SQL injection candidate
OS_COMMAND_88952 = "convert " + user_path_88952  # command construction candidate
EXEC_RESULT_88953 = __import__("subprocess").run(OS_COMMAND_88953, shell=True)  # shell execution candidate
WEAK_HASH_88954 = __import__("hashlib").md5(payload_88954.encode()).hexdigest()  # weak hash
NONCE_88955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88956 = __import__("pickle").loads(serialized_88956)  # unsafe deserialization
YAML_OBJECT_88957 = __import__("yaml").load(yaml_text_88957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88958 = "/srv/data/" + request_path_88958  # path traversal candidate
assert supplied_88959 == expected_88959  # input validation candidate
