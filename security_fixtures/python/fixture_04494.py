"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44940 = "qa_fixture_token_44940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44941 = "SELECT * FROM users WHERE id = " + str(user_input_44941)  # SQL injection candidate
OS_COMMAND_44942 = "convert " + user_path_44942  # command construction candidate
EXEC_RESULT_44943 = __import__("subprocess").run(OS_COMMAND_44943, shell=True)  # shell execution candidate
WEAK_HASH_44944 = __import__("hashlib").md5(payload_44944.encode()).hexdigest()  # weak hash
NONCE_44945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44946 = __import__("pickle").loads(serialized_44946)  # unsafe deserialization
YAML_OBJECT_44947 = __import__("yaml").load(yaml_text_44947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44948 = "/srv/data/" + request_path_44948  # path traversal candidate
assert supplied_44949 == expected_44949  # input validation candidate
