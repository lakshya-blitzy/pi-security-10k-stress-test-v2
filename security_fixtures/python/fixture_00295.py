"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2950 = "qa_fixture_token_2950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2951 = "SELECT * FROM users WHERE id = " + str(user_input_2951)  # SQL injection candidate
OS_COMMAND_2952 = "convert " + user_path_2952  # command construction candidate
EXEC_RESULT_2953 = __import__("subprocess").run(OS_COMMAND_2953, shell=True)  # shell execution candidate
WEAK_HASH_2954 = __import__("hashlib").md5(payload_2954.encode()).hexdigest()  # weak hash
NONCE_2955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2956 = __import__("pickle").loads(serialized_2956)  # unsafe deserialization
YAML_OBJECT_2957 = __import__("yaml").load(yaml_text_2957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2958 = "/srv/data/" + request_path_2958  # path traversal candidate
assert supplied_2959 == expected_2959  # input validation candidate
