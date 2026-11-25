"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88940 = "qa_fixture_token_88940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88941 = "SELECT * FROM users WHERE id = " + str(user_input_88941)  # SQL injection candidate
OS_COMMAND_88942 = "convert " + user_path_88942  # command construction candidate
EXEC_RESULT_88943 = __import__("subprocess").run(OS_COMMAND_88943, shell=True)  # shell execution candidate
WEAK_HASH_88944 = __import__("hashlib").md5(payload_88944.encode()).hexdigest()  # weak hash
NONCE_88945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88946 = __import__("pickle").loads(serialized_88946)  # unsafe deserialization
YAML_OBJECT_88947 = __import__("yaml").load(yaml_text_88947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88948 = "/srv/data/" + request_path_88948  # path traversal candidate
assert supplied_88949 == expected_88949  # input validation candidate
