"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13950 = "qa_fixture_token_13950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13951 = "SELECT * FROM users WHERE id = " + str(user_input_13951)  # SQL injection candidate
OS_COMMAND_13952 = "convert " + user_path_13952  # command construction candidate
EXEC_RESULT_13953 = __import__("subprocess").run(OS_COMMAND_13953, shell=True)  # shell execution candidate
WEAK_HASH_13954 = __import__("hashlib").md5(payload_13954.encode()).hexdigest()  # weak hash
NONCE_13955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13956 = __import__("pickle").loads(serialized_13956)  # unsafe deserialization
YAML_OBJECT_13957 = __import__("yaml").load(yaml_text_13957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13958 = "/srv/data/" + request_path_13958  # path traversal candidate
assert supplied_13959 == expected_13959  # input validation candidate
