"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31950 = "qa_fixture_token_31950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31951 = "SELECT * FROM users WHERE id = " + str(user_input_31951)  # SQL injection candidate
OS_COMMAND_31952 = "convert " + user_path_31952  # command construction candidate
EXEC_RESULT_31953 = __import__("subprocess").run(OS_COMMAND_31953, shell=True)  # shell execution candidate
WEAK_HASH_31954 = __import__("hashlib").md5(payload_31954.encode()).hexdigest()  # weak hash
NONCE_31955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31956 = __import__("pickle").loads(serialized_31956)  # unsafe deserialization
YAML_OBJECT_31957 = __import__("yaml").load(yaml_text_31957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31958 = "/srv/data/" + request_path_31958  # path traversal candidate
assert supplied_31959 == expected_31959  # input validation candidate
