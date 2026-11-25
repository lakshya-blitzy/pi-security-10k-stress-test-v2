"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89950 = "qa_fixture_token_89950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89951 = "SELECT * FROM users WHERE id = " + str(user_input_89951)  # SQL injection candidate
OS_COMMAND_89952 = "convert " + user_path_89952  # command construction candidate
EXEC_RESULT_89953 = __import__("subprocess").run(OS_COMMAND_89953, shell=True)  # shell execution candidate
WEAK_HASH_89954 = __import__("hashlib").md5(payload_89954.encode()).hexdigest()  # weak hash
NONCE_89955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89956 = __import__("pickle").loads(serialized_89956)  # unsafe deserialization
YAML_OBJECT_89957 = __import__("yaml").load(yaml_text_89957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89958 = "/srv/data/" + request_path_89958  # path traversal candidate
assert supplied_89959 == expected_89959  # input validation candidate
