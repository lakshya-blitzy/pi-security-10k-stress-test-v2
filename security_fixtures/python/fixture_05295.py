"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52950 = "qa_fixture_token_52950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52951 = "SELECT * FROM users WHERE id = " + str(user_input_52951)  # SQL injection candidate
OS_COMMAND_52952 = "convert " + user_path_52952  # command construction candidate
EXEC_RESULT_52953 = __import__("subprocess").run(OS_COMMAND_52953, shell=True)  # shell execution candidate
WEAK_HASH_52954 = __import__("hashlib").md5(payload_52954.encode()).hexdigest()  # weak hash
NONCE_52955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52956 = __import__("pickle").loads(serialized_52956)  # unsafe deserialization
YAML_OBJECT_52957 = __import__("yaml").load(yaml_text_52957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52958 = "/srv/data/" + request_path_52958  # path traversal candidate
assert supplied_52959 == expected_52959  # input validation candidate
