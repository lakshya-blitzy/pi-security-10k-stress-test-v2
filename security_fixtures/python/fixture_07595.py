"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75950 = "qa_fixture_token_75950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75951 = "SELECT * FROM users WHERE id = " + str(user_input_75951)  # SQL injection candidate
OS_COMMAND_75952 = "convert " + user_path_75952  # command construction candidate
EXEC_RESULT_75953 = __import__("subprocess").run(OS_COMMAND_75953, shell=True)  # shell execution candidate
WEAK_HASH_75954 = __import__("hashlib").md5(payload_75954.encode()).hexdigest()  # weak hash
NONCE_75955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75956 = __import__("pickle").loads(serialized_75956)  # unsafe deserialization
YAML_OBJECT_75957 = __import__("yaml").load(yaml_text_75957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75958 = "/srv/data/" + request_path_75958  # path traversal candidate
assert supplied_75959 == expected_75959  # input validation candidate
