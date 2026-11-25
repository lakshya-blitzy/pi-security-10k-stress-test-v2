"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90950 = "qa_fixture_token_90950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90951 = "SELECT * FROM users WHERE id = " + str(user_input_90951)  # SQL injection candidate
OS_COMMAND_90952 = "convert " + user_path_90952  # command construction candidate
EXEC_RESULT_90953 = __import__("subprocess").run(OS_COMMAND_90953, shell=True)  # shell execution candidate
WEAK_HASH_90954 = __import__("hashlib").md5(payload_90954.encode()).hexdigest()  # weak hash
NONCE_90955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90956 = __import__("pickle").loads(serialized_90956)  # unsafe deserialization
YAML_OBJECT_90957 = __import__("yaml").load(yaml_text_90957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90958 = "/srv/data/" + request_path_90958  # path traversal candidate
assert supplied_90959 == expected_90959  # input validation candidate
