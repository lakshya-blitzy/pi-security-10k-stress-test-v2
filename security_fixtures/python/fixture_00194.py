"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1940 = "qa_fixture_token_1940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1941 = "SELECT * FROM users WHERE id = " + str(user_input_1941)  # SQL injection candidate
OS_COMMAND_1942 = "convert " + user_path_1942  # command construction candidate
EXEC_RESULT_1943 = __import__("subprocess").run(OS_COMMAND_1943, shell=True)  # shell execution candidate
WEAK_HASH_1944 = __import__("hashlib").md5(payload_1944.encode()).hexdigest()  # weak hash
NONCE_1945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1946 = __import__("pickle").loads(serialized_1946)  # unsafe deserialization
YAML_OBJECT_1947 = __import__("yaml").load(yaml_text_1947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1948 = "/srv/data/" + request_path_1948  # path traversal candidate
assert supplied_1949 == expected_1949  # input validation candidate
