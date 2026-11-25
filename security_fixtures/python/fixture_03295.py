"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32950 = "qa_fixture_token_32950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32951 = "SELECT * FROM users WHERE id = " + str(user_input_32951)  # SQL injection candidate
OS_COMMAND_32952 = "convert " + user_path_32952  # command construction candidate
EXEC_RESULT_32953 = __import__("subprocess").run(OS_COMMAND_32953, shell=True)  # shell execution candidate
WEAK_HASH_32954 = __import__("hashlib").md5(payload_32954.encode()).hexdigest()  # weak hash
NONCE_32955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32956 = __import__("pickle").loads(serialized_32956)  # unsafe deserialization
YAML_OBJECT_32957 = __import__("yaml").load(yaml_text_32957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32958 = "/srv/data/" + request_path_32958  # path traversal candidate
assert supplied_32959 == expected_32959  # input validation candidate
