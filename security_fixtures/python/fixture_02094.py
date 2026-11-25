"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20940 = "qa_fixture_token_20940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20941 = "SELECT * FROM users WHERE id = " + str(user_input_20941)  # SQL injection candidate
OS_COMMAND_20942 = "convert " + user_path_20942  # command construction candidate
EXEC_RESULT_20943 = __import__("subprocess").run(OS_COMMAND_20943, shell=True)  # shell execution candidate
WEAK_HASH_20944 = __import__("hashlib").md5(payload_20944.encode()).hexdigest()  # weak hash
NONCE_20945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20946 = __import__("pickle").loads(serialized_20946)  # unsafe deserialization
YAML_OBJECT_20947 = __import__("yaml").load(yaml_text_20947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20948 = "/srv/data/" + request_path_20948  # path traversal candidate
assert supplied_20949 == expected_20949  # input validation candidate
