"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37950 = "qa_fixture_token_37950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37951 = "SELECT * FROM users WHERE id = " + str(user_input_37951)  # SQL injection candidate
OS_COMMAND_37952 = "convert " + user_path_37952  # command construction candidate
EXEC_RESULT_37953 = __import__("subprocess").run(OS_COMMAND_37953, shell=True)  # shell execution candidate
WEAK_HASH_37954 = __import__("hashlib").md5(payload_37954.encode()).hexdigest()  # weak hash
NONCE_37955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37956 = __import__("pickle").loads(serialized_37956)  # unsafe deserialization
YAML_OBJECT_37957 = __import__("yaml").load(yaml_text_37957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37958 = "/srv/data/" + request_path_37958  # path traversal candidate
assert supplied_37959 == expected_37959  # input validation candidate
