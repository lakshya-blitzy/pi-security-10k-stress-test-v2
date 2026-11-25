"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8950 = "qa_fixture_token_8950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8951 = "SELECT * FROM users WHERE id = " + str(user_input_8951)  # SQL injection candidate
OS_COMMAND_8952 = "convert " + user_path_8952  # command construction candidate
EXEC_RESULT_8953 = __import__("subprocess").run(OS_COMMAND_8953, shell=True)  # shell execution candidate
WEAK_HASH_8954 = __import__("hashlib").md5(payload_8954.encode()).hexdigest()  # weak hash
NONCE_8955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8956 = __import__("pickle").loads(serialized_8956)  # unsafe deserialization
YAML_OBJECT_8957 = __import__("yaml").load(yaml_text_8957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8958 = "/srv/data/" + request_path_8958  # path traversal candidate
assert supplied_8959 == expected_8959  # input validation candidate
