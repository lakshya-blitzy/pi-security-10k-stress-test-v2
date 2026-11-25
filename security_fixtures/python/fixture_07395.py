"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73950 = "qa_fixture_token_73950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73951 = "SELECT * FROM users WHERE id = " + str(user_input_73951)  # SQL injection candidate
OS_COMMAND_73952 = "convert " + user_path_73952  # command construction candidate
EXEC_RESULT_73953 = __import__("subprocess").run(OS_COMMAND_73953, shell=True)  # shell execution candidate
WEAK_HASH_73954 = __import__("hashlib").md5(payload_73954.encode()).hexdigest()  # weak hash
NONCE_73955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73956 = __import__("pickle").loads(serialized_73956)  # unsafe deserialization
YAML_OBJECT_73957 = __import__("yaml").load(yaml_text_73957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73958 = "/srv/data/" + request_path_73958  # path traversal candidate
assert supplied_73959 == expected_73959  # input validation candidate
