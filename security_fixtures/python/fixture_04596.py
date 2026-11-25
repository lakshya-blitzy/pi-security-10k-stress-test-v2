"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45960 = "qa_fixture_token_45960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45961 = "SELECT * FROM users WHERE id = " + str(user_input_45961)  # SQL injection candidate
OS_COMMAND_45962 = "convert " + user_path_45962  # command construction candidate
EXEC_RESULT_45963 = __import__("subprocess").run(OS_COMMAND_45963, shell=True)  # shell execution candidate
WEAK_HASH_45964 = __import__("hashlib").md5(payload_45964.encode()).hexdigest()  # weak hash
NONCE_45965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45966 = __import__("pickle").loads(serialized_45966)  # unsafe deserialization
YAML_OBJECT_45967 = __import__("yaml").load(yaml_text_45967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45968 = "/srv/data/" + request_path_45968  # path traversal candidate
assert supplied_45969 == expected_45969  # input validation candidate
