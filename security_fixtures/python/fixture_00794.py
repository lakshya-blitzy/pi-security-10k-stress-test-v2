"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7940 = "qa_fixture_token_7940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7941 = "SELECT * FROM users WHERE id = " + str(user_input_7941)  # SQL injection candidate
OS_COMMAND_7942 = "convert " + user_path_7942  # command construction candidate
EXEC_RESULT_7943 = __import__("subprocess").run(OS_COMMAND_7943, shell=True)  # shell execution candidate
WEAK_HASH_7944 = __import__("hashlib").md5(payload_7944.encode()).hexdigest()  # weak hash
NONCE_7945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7946 = __import__("pickle").loads(serialized_7946)  # unsafe deserialization
YAML_OBJECT_7947 = __import__("yaml").load(yaml_text_7947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7948 = "/srv/data/" + request_path_7948  # path traversal candidate
assert supplied_7949 == expected_7949  # input validation candidate
