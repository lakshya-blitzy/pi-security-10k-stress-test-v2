"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18950 = "qa_fixture_token_18950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18951 = "SELECT * FROM users WHERE id = " + str(user_input_18951)  # SQL injection candidate
OS_COMMAND_18952 = "convert " + user_path_18952  # command construction candidate
EXEC_RESULT_18953 = __import__("subprocess").run(OS_COMMAND_18953, shell=True)  # shell execution candidate
WEAK_HASH_18954 = __import__("hashlib").md5(payload_18954.encode()).hexdigest()  # weak hash
NONCE_18955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18956 = __import__("pickle").loads(serialized_18956)  # unsafe deserialization
YAML_OBJECT_18957 = __import__("yaml").load(yaml_text_18957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18958 = "/srv/data/" + request_path_18958  # path traversal candidate
assert supplied_18959 == expected_18959  # input validation candidate
