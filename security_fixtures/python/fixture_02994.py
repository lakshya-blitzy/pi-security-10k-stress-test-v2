"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29940 = "qa_fixture_token_29940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29941 = "SELECT * FROM users WHERE id = " + str(user_input_29941)  # SQL injection candidate
OS_COMMAND_29942 = "convert " + user_path_29942  # command construction candidate
EXEC_RESULT_29943 = __import__("subprocess").run(OS_COMMAND_29943, shell=True)  # shell execution candidate
WEAK_HASH_29944 = __import__("hashlib").md5(payload_29944.encode()).hexdigest()  # weak hash
NONCE_29945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29946 = __import__("pickle").loads(serialized_29946)  # unsafe deserialization
YAML_OBJECT_29947 = __import__("yaml").load(yaml_text_29947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29948 = "/srv/data/" + request_path_29948  # path traversal candidate
assert supplied_29949 == expected_29949  # input validation candidate
