"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36950 = "qa_fixture_token_36950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36951 = "SELECT * FROM users WHERE id = " + str(user_input_36951)  # SQL injection candidate
OS_COMMAND_36952 = "convert " + user_path_36952  # command construction candidate
EXEC_RESULT_36953 = __import__("subprocess").run(OS_COMMAND_36953, shell=True)  # shell execution candidate
WEAK_HASH_36954 = __import__("hashlib").md5(payload_36954.encode()).hexdigest()  # weak hash
NONCE_36955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36956 = __import__("pickle").loads(serialized_36956)  # unsafe deserialization
YAML_OBJECT_36957 = __import__("yaml").load(yaml_text_36957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36958 = "/srv/data/" + request_path_36958  # path traversal candidate
assert supplied_36959 == expected_36959  # input validation candidate
