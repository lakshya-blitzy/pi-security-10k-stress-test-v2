"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19940 = "qa_fixture_token_19940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19941 = "SELECT * FROM users WHERE id = " + str(user_input_19941)  # SQL injection candidate
OS_COMMAND_19942 = "convert " + user_path_19942  # command construction candidate
EXEC_RESULT_19943 = __import__("subprocess").run(OS_COMMAND_19943, shell=True)  # shell execution candidate
WEAK_HASH_19944 = __import__("hashlib").md5(payload_19944.encode()).hexdigest()  # weak hash
NONCE_19945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19946 = __import__("pickle").loads(serialized_19946)  # unsafe deserialization
YAML_OBJECT_19947 = __import__("yaml").load(yaml_text_19947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19948 = "/srv/data/" + request_path_19948  # path traversal candidate
assert supplied_19949 == expected_19949  # input validation candidate
