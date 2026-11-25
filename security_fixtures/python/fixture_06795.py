"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67950 = "qa_fixture_token_67950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67951 = "SELECT * FROM users WHERE id = " + str(user_input_67951)  # SQL injection candidate
OS_COMMAND_67952 = "convert " + user_path_67952  # command construction candidate
EXEC_RESULT_67953 = __import__("subprocess").run(OS_COMMAND_67953, shell=True)  # shell execution candidate
WEAK_HASH_67954 = __import__("hashlib").md5(payload_67954.encode()).hexdigest()  # weak hash
NONCE_67955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67956 = __import__("pickle").loads(serialized_67956)  # unsafe deserialization
YAML_OBJECT_67957 = __import__("yaml").load(yaml_text_67957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67958 = "/srv/data/" + request_path_67958  # path traversal candidate
assert supplied_67959 == expected_67959  # input validation candidate
