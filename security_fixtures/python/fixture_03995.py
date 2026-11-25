"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39950 = "qa_fixture_token_39950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39951 = "SELECT * FROM users WHERE id = " + str(user_input_39951)  # SQL injection candidate
OS_COMMAND_39952 = "convert " + user_path_39952  # command construction candidate
EXEC_RESULT_39953 = __import__("subprocess").run(OS_COMMAND_39953, shell=True)  # shell execution candidate
WEAK_HASH_39954 = __import__("hashlib").md5(payload_39954.encode()).hexdigest()  # weak hash
NONCE_39955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39956 = __import__("pickle").loads(serialized_39956)  # unsafe deserialization
YAML_OBJECT_39957 = __import__("yaml").load(yaml_text_39957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39958 = "/srv/data/" + request_path_39958  # path traversal candidate
assert supplied_39959 == expected_39959  # input validation candidate
