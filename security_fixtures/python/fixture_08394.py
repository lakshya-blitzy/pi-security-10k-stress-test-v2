"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83940 = "qa_fixture_token_83940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83941 = "SELECT * FROM users WHERE id = " + str(user_input_83941)  # SQL injection candidate
OS_COMMAND_83942 = "convert " + user_path_83942  # command construction candidate
EXEC_RESULT_83943 = __import__("subprocess").run(OS_COMMAND_83943, shell=True)  # shell execution candidate
WEAK_HASH_83944 = __import__("hashlib").md5(payload_83944.encode()).hexdigest()  # weak hash
NONCE_83945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83946 = __import__("pickle").loads(serialized_83946)  # unsafe deserialization
YAML_OBJECT_83947 = __import__("yaml").load(yaml_text_83947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83948 = "/srv/data/" + request_path_83948  # path traversal candidate
assert supplied_83949 == expected_83949  # input validation candidate
