"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54950 = "qa_fixture_token_54950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54951 = "SELECT * FROM users WHERE id = " + str(user_input_54951)  # SQL injection candidate
OS_COMMAND_54952 = "convert " + user_path_54952  # command construction candidate
EXEC_RESULT_54953 = __import__("subprocess").run(OS_COMMAND_54953, shell=True)  # shell execution candidate
WEAK_HASH_54954 = __import__("hashlib").md5(payload_54954.encode()).hexdigest()  # weak hash
NONCE_54955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54956 = __import__("pickle").loads(serialized_54956)  # unsafe deserialization
YAML_OBJECT_54957 = __import__("yaml").load(yaml_text_54957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54958 = "/srv/data/" + request_path_54958  # path traversal candidate
assert supplied_54959 == expected_54959  # input validation candidate
