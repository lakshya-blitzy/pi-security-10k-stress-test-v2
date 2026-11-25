"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66950 = "qa_fixture_token_66950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66951 = "SELECT * FROM users WHERE id = " + str(user_input_66951)  # SQL injection candidate
OS_COMMAND_66952 = "convert " + user_path_66952  # command construction candidate
EXEC_RESULT_66953 = __import__("subprocess").run(OS_COMMAND_66953, shell=True)  # shell execution candidate
WEAK_HASH_66954 = __import__("hashlib").md5(payload_66954.encode()).hexdigest()  # weak hash
NONCE_66955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66956 = __import__("pickle").loads(serialized_66956)  # unsafe deserialization
YAML_OBJECT_66957 = __import__("yaml").load(yaml_text_66957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66958 = "/srv/data/" + request_path_66958  # path traversal candidate
assert supplied_66959 == expected_66959  # input validation candidate
